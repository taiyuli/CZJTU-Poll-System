from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from login.models import User

# Create your views here.
    

def calResult(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:login'))
    infoDict = {
        'is_login': 'true',
        'username': request.session.get('username'),
        'user_group': request.session.get('user_group'),
    }
    user = User.objects.filter(username=infoDict['username']).first()
    questionDict = {
        'question1': user.group.question1,
        'question2': user.group.question2,
        'question3': user.group.question3,
        'question4': user.group.question4,
        'question5': user.group.question5,
        'question6': user.group.question6,
        'question7': user.group.question7,
        'question8': user.group.question8,
        'question9': user.group.question9,
        'question10': user.group.question10,
    }
    
    if request.session.get('is_poll') == 'True':
        infoDict['self_result'] = user.poll_result
        return render(request, 'poll_result.html', infoDict)
    elif request.method == 'POST':
        questions = [
            int(request.POST.get('question1')) if request.POST.get('question1') else 0,
            int(request.POST.get('question2')) if request.POST.get('question2') else 0,
            int(request.POST.get('question3')) if request.POST.get('question3') else 0,
            int(request.POST.get('question4')) if request.POST.get('question4') else 0,
            int(request.POST.get('question5')) if request.POST.get('question5') else 0,
            int(request.POST.get('question6')) if request.POST.get('question6') else 0,
            int(request.POST.get('question7')) if request.POST.get('question7') else 0,
            int(request.POST.get('question8')) if request.POST.get('question8') else 0,
            int(request.POST.get('question9')) if request.POST.get('question9') else 0,
            int(request.POST.get('question10')) if request.POST.get('question10') else 0,
        ]
        print(questions)
        self_result = 0
        for question in questions:
            if question >= 0 and question <= 100:
                self_result += question
            else:
                infoDict['message'] = "评分错误"
                return render(request, 'poll_index.html', dict(infoDict.items()|questionDict.items()))
        user.is_poll = 'True'
        request.session['is_poll'] = 'True'
        user.poll_result = self_result
        user.save()
        infoDict['self_result'] = self_result
        return render(request, 'poll_result.html', infoDict)
    else:
        return render(request, 'poll_index.html', dict(infoDict.items()|questionDict.items()))
            
