from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    infoDict = {
        'is_login': 'flase',
        'username': request.session.get('username'),
        'user_group': request.session.get('user_group'),
    }
    if request.session.get('is_login'):
        infoDict['is_login'] = 'true'
    
    return render(request, 'index.html', infoDict)