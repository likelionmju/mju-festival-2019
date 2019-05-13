from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# register
def register(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']
        password2 = request.POST['confirm-pw']

        check1 = exist_user_check(username)
        check2 = password_check(password, password2)

        if check1 and check2:
            user = User.objects.create_user(
                username, password
            )
            auth.login(request, user)
            return redirect('home')
        elif not check1:
            message = "이미 존재하는 아이디입니다"
            return render(request, 'register.html', {'message':message})
        elif not check2: 
            message = "비밀번호를 확인하세요"
            return render(request, 'register.html', {'message':message})
    else:
        return render(request, 'register.html')

def exist_user_check(username):
    if not User.objects.filter(username=username).exists():
        return True
    else: 
        return False

def password_check(password, password2):
    if password == password2:
        return True
    else:
        return False


def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect ('home')
        else:
            message="로그인 정보를 확인하세요"
            return render(request, 'login.html', {'message':message})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')