from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import copy

from login.models import User, PollData
from poll.models import WorkGroup

# Create your views here.


# 计算评价
def calResult(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:login'))
    infoDict = {
        'is_login': 'true',
        'username': request.session.get('username'),
        'user_group': request.session.get('user_group'),
    }
    user = User.objects.filter(username=infoDict['username']).first()
    
    if request.session.get('is_poll') == 'True':
        poll_result = PollData.objects.filter(user__username=infoDict['username']).first()
        if not poll_result:
            if request.session.get('is_login'):
                request.session.flush()
            return redirect(reverse('login:login'))
        infoDict['question1'] = poll_result.question1
        infoDict['question2'] = poll_result.question2
        infoDict['question3'] = poll_result.question3
        infoDict['question4'] = poll_result.question4
        infoDict['question5'] = poll_result.question5
        infoDict['reason'] = poll_result.reason if poll_result.reason else False
        return render(request, 'poll_result.html', infoDict)
    elif request.method == 'POST':
        questions = [
            'nothing',
            request.POST.get('question1') if request.POST.get('question1') else '0',
            request.POST.get('question2') if request.POST.get('question2') else '0',
            request.POST.get('question3') if request.POST.get('question3') else '0',
            request.POST.get('question4') if request.POST.get('question4') else '0',
            request.POST.get('question5') if request.POST.get('question5') else '0',
        ]
        for question_result in questions:
            if question_result == '0':
                infoDict['message'] = "评分错误"
                return render(request, 'poll_index.html', infoDict)
        poll_result = PollData(user=user, group=user.group, question1=questions[1], question2=questions[2], question3=questions[3], question4=questions[4], question5=questions[5])
        user.is_poll = 'True'
        request.session['is_poll'] = 'True'
        poll_result.save()
        user.save()
        if questions[1] == "不合格" and questions[2] == "不合格" and questions[3] == "不合格" and questions[4] == "不合格" and questions[5] == "不合格":
            return redirect(reverse('poll:poll_reason'))
        infoDict['question1'] = poll_result.question1
        infoDict['question2'] = poll_result.question2
        infoDict['question3'] = poll_result.question3
        infoDict['question4'] = poll_result.question4
        infoDict['question5'] = poll_result.question5
        return render(request, 'poll_result.html', infoDict)
    else:
        return render(request, 'poll_index.html', infoDict)
            

# 显示和处理评价理由
def pollReason(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:login'))
    infoDict = {
        'is_login': 'true',
        'username': request.session.get('username'),
        'user_group': request.session.get('user_group'),
    }

    if request.session.get('is_poll') == 'True':
        if request.method == 'POST':
            pollReason = request.POST.get('pollReason')
            if pollReason:
                poll_result = PollData.objects.filter(user__username=infoDict['username']).first()
                if poll_result:
                    poll_result.reason = pollReason
                    poll_result.save()
                    return redirect(reverse('poll:poll_index'))
                else:
                    return redirect(reverse('poll:poll_index'))
            else:
                infoDict['message'] = "理由错误"
                return render(request, 'poll_reason.html', infoDict)
        return render(request, 'poll_reason.html', infoDict)
    else:
        return redirect(reverse('poll:poll_index'))


# 计算统计结果，并展示
@login_required(login_url='/admin/')
def adminResultView(request):
    groupQuerySet = WorkGroup.objects.all()
    groupList = []
    for groupQuery in groupQuerySet:
        groupList.append(groupQuery.groupName)
    infoDict = {
        'groupList': groupList,
        'currentQueryGroup': None,
    }
    if request.method == 'POST':
        target_group = request.POST.get('target_group')
        infoDict['currentQueryGroup'] = target_group
        infoDict['userCount'] = User.objects.filter(group__groupName=target_group).count()
        queryResultSet = PollData.objects.filter(group__groupName=target_group)
        queryResultCount = queryResultSet.count()
        if queryResultCount <= 0:
            infoDict['is_query_result'] = False
            infoDict['message'] = "无数据"
            return render(request, 'admin_poll_view.html', infoDict)
        infoDict['queryResultCount'] = queryResultCount
        questionsGrade = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]
        queryResultList = []
        for queryResult in queryResultSet:
            queryResultList.append([queryResult.question1, queryResult.question2, queryResult.question3, queryResult.question4, queryResult.question5])
        for i in range(5):
            for queryResult in queryResultList:
                if queryResult[i] == "优秀":
                    questionsGrade[i][0] += 1
                elif queryResult[i] == "合格":
                    questionsGrade[i][1] += 1
                elif queryResult[i] == "基本合格":
                    questionsGrade[i][2] += 1
                elif queryResult[i] == "不合格":
                    questionsGrade[i][3] += 1
        infoDict['questionsGrade'] = questionsGrade
        questionsGradePercent = copy.deepcopy(questionsGrade)
        for i in range(5):
            questionsGradePercent[i] = [round(x * 100 / queryResultCount, 2) for x in questionsGradePercent[i]][:]
        infoDict['questionsGradePercent'] = questionsGradePercent
        questionsGradeSummary = [0, 0, 0, 0]
        for i in range(4):
            for questionGrade in questionsGrade:
                questionsGradeSummary[i] += questionGrade[i]
        questionsGradeSummaryPercent = copy.deepcopy(questionsGradeSummary)
        for i in range(4):
            questionsGradeSummaryPercent[i] = round(questionsGradeSummaryPercent[i] / (queryResultCount * 5) * 100, 2)
        infoDict['questionsGradeSummary'] = questionsGradeSummary
        infoDict['questionsGradeSummaryPercent'] = questionsGradeSummaryPercent  

        pollResultReason = []
        for queryResult in queryResultSet:
            if queryResult.reason:
                pollResultReason.append(queryResult.reason)
        infoDict['pollResultReason'] = pollResultReason

        infoDict['is_query_result'] = True
        return render(request, 'admin_poll_view.html', infoDict)
    else:
        infoDict['is_query_result'] = False
        return render(request, 'admin_poll_view.html', infoDict)
    
    
