from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

from .models import User

# Create your views here.

# 登陆
def login(request):
    if request.session.get('is_login'):
        return redirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        if username and password:
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['is_login'] = True
                request.session['username'] = user.username
                request.session['user_group'] = user.group.groupName
                request.session['is_poll'] = user.is_poll
                return redirect(reverse('index'))
            else:
                message = "用户名或密码错误"
                return render(request, 'login.html', {'message': message})
        else:
            message = "用户名或密码错误"
            return render(request, 'login.html', {'message': message})
    return render(request, "login.html")


# 登出
def logout(request):
    if request.session.get('is_login'):
        request.session.flush()
    return redirect(reverse('login:login'))


# 修改
def modify(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:login'))
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        old_password = request.POST.get('old_password').strip()
        new_password = request.POST.get('new_password').strip()
        if username and old_password and new_password:
            user = User.objects.filter(username=username, password=old_password).first()
            if user:
                user.password = new_password
                user.save()
                if request.session.get('is_login'):
                    request.session.flush()
                return redirect(reverse('login:login'))
            else:
                message = "用户名或原密码错误"
                return render(request, 'modify.html', {'message': message})
        else:
            message = "用户名或原密码错误"
            return render(request, 'modify.html', {'message': message})
    return render(request, "modify.html")