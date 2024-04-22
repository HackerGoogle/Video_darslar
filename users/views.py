from django.shortcuts import render,redirect
from django.urls import reverse
from .form import SignUpForm,LogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def login_required_decorator(func):
    return login_required(func, login_url="login")

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect(reverse('video_dars_app:home'))

def signup(request):
    sign=SignUpForm()
    if request.method == 'POST':
        sign=SignUpForm(request.POST, request.FILES)
        if sign.is_valid():
            sign.save()
            return redirect(reverse('video_dars_app:home'))
    return render(request, "auth/signup.html", {'sign':sign})

def login_page(request):
    errors=""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect(reverse('video_dars_app:home'))
        else:
            errors+="Login yoki parol noto'g'ri. Iltimos qaytadan kiriting!"
            return render(request, "auth/login1.html",{"errors":errors})

    return render(request, "auth/login1.html",{"errors":errors})


@login_required_decorator
def home_page(request):
    return render(request, 'home.html')
