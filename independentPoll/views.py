from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, LeaderModel, LeaderPollDataModel, DepartmentModel, DepartmentPollDataModel

# Create your views here.


def leaderPollIdpd(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:login'))
    infoDict = {
        'is_login': 'true',
        'username': request.session.get('username'),
        'user_group': request.session.get('user_group'),
    }
    user = User.objects.filter(username=infoDict['username']).first()
    to_poll_leaders = user.leadermodel_set.all()
    to_poll_leader_list = []
    for to_poll_leader in to_poll_leaders:
        to_poll_leader_list.append([to_poll_leader.name, None])
    infoDict['to_poll_leader_list'] = to_poll_leader_list

    if user.is_poll_2 == 'True':
        leaderPollQueryDatas = LeaderPollDataModel.objects.filter(user__username=user.username)
        if not leaderPollQueryDatas:
            user.is_poll_2 = 'False'
            user.save(update_fields=['is_poll_2'])
            return redirect(reverse('independentPoll:leader_poll'))
        infoDict['to_poll_leader_list'] = []
        for leaderPollQueryData in leaderPollQueryDatas:
            infoDict['to_poll_leader_list'].append([leaderPollQueryData.leader.name, leaderPollQueryData.pollGrade])
        return render(request, 'leader_poll_result.html', infoDict)
    elif request.method == 'POST':
        for to_poll_leader in to_poll_leader_list:
            to_poll_leader[1] = request.POST.get(to_poll_leader[0])
            if not to_poll_leader[1]:
                infoDict['message'] = "评价错误"
                return redirect(reverse('independentPoll:leader_poll'))
        for to_poll_leader in to_poll_leader_list:
            pollResult = LeaderPollDataModel(user=user, leader=LeaderModel.objects.get(name=to_poll_leader[0]), pollGrade=to_poll_leader[1])
            pollResult.save()
        user.is_poll_2 = 'True'
        user.save(update_fields=['is_poll_2'])
        infoDict['to_poll_leader_list'] = to_poll_leader_list
        return render(request, 'leader_poll_result.html', infoDict)
    return render(request, 'leader_poll.html', infoDict)


def departmentPollIdpd(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:login'))
    infoDict = {
        'is_login': 'true',
        'username': request.session.get('username'),
        'user_group': request.session.get('user_group'),
    }
    user = User.objects.filter(username=infoDict['username']).first()
    to_poll_departments = user.departmentmodel_set.all()
    to_poll_department_list = []
    for to_poll_department in to_poll_departments:
        to_poll_department_list.append([to_poll_department.name, None])
    infoDict['to_poll_department_list'] = to_poll_department_list

    if user.is_poll_3 == 'True':
        departmentPollQueryDatas = DepartmentPollDataModel.objects.filter(user__username=user.username)
        if not departmentPollQueryDatas:
            user.is_poll_3 = 'False'
            user.save(update_fields=['is_poll_3'])
            return redirect(reverse('independentPoll:department_poll'))
        infoDict['to_poll_department_list'] = []
        for departmentPollQueryData in departmentPollQueryDatas:
            infoDict['to_poll_department_list'].append([departmentPollQueryData.department.name, departmentPollQueryData.pollGrade])
        return render(request, 'department_poll_result.html', infoDict)
    elif request.method == 'POST':
        for to_poll_department in to_poll_department_list:
            to_poll_department[1] = request.POST.get(to_poll_department[0])
            if not to_poll_department[1]:
                infoDict['message'] = "评价错误"
                return redirect(reverse('independentPoll:department_poll'))
        for to_poll_department in to_poll_department_list:
            pollResult = DepartmentPollDataModel(user=user, department=DepartmentModel.objects.get(name=to_poll_department[0]), pollGrade=to_poll_department[1])
            pollResult.save()
        user.is_poll_3 = 'True'
        user.save(update_fields=['is_poll_3'])
        infoDict['to_poll_department_list'] = to_poll_department_list
        return render(request, 'department_poll_result.html', infoDict)
    return render(request, 'department_poll.html', infoDict)


@login_required(login_url='/admin/')
def leaderPollIdpdCount(request):
    leaderQuerySet = LeaderModel.objects.all()
    leaderList = []
    for leaderQuery in leaderQuerySet:
        leaderList.append([leaderQuery.name, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for leader in leaderList:
        leaderPollDatas = LeaderPollDataModel.objects.filter(leader__name=leader[0])
        for leaderPollData in leaderPollDatas:
            leader[5] += 1
            if leaderPollData.pollGrade == '优秀':
                leader[1] += 1
            elif leaderPollData.pollGrade == '合格':
                leader[2] += 1
            elif leaderPollData.pollGrade == '基本合格':
                leader[3] += 1
            elif leaderPollData.pollGrade == '不合格':
                leader[4] += 1
        if leader[5] != 0:
            leader[6] = round(leader[1] / leader[5] * 100, 2)
            leader[7] = round(leader[2] / leader[5] * 100, 2)
            leader[8] = round(leader[3] / leader[5] * 100, 2)
            leader[9] = round(leader[4] / leader[5] * 100, 2)
    infoDict = {
        'leaderList': leaderList
    }
    return render(request, 'leader_poll_count.html', infoDict)


@login_required(login_url='/admin/')
def departmentPollIdpdCount(request):
    departmentQuerySet = DepartmentModel.objects.all()
    departmentList = []
    for departmentQuery in departmentQuerySet:
        departmentList.append([departmentQuery.name, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for department in departmentList:
        departmentPollDatas = DepartmentPollDataModel.objects.filter(department__name=department[0])
        for departmentPollData in departmentPollDatas:
            department[5] += 1
            if departmentPollData.pollGrade == '优秀':
                department[1] += 1
            elif departmentPollData.pollGrade == '合格':
                department[2] += 1
            elif departmentPollData.pollGrade == '基本合格':
                department[3] += 1
            elif departmentPollData.pollGrade == '不合格':
                department[4] += 1
        if department[5] != 0:
            department[6] = round(department[1] / department[5] * 100, 2)
            department[7] = round(department[2] / department[5] * 100, 2)
            department[8] = round(department[3] / department[5] * 100, 2)
            department[9] = round(department[4] / department[5] * 100, 2)
    infoDict = {
        'departmentList': departmentList
    }
    return render(request, 'department_poll_count.html', infoDict)