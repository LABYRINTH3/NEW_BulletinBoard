from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm, UserSignupForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user: # 만약 유저가 존재해서 로그인이 되면
                return redirect('home')  # 로그인 후 이동하는 페이지
            else:
                messages.error(request, '아이디 또는 비밀번호가 일치하지 않습니다.')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')  # 회원가입 후 로그인 페이지로 이동
    else:
        form = UserSignupForm()
    return render(request, 'account/createaccount.html', {'form': form})
