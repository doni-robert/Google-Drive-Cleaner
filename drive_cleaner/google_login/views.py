from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated:
        context = {'name': request.user.username}
        return render(request, "google_login/home.html", context)
    
    return redirect('/login')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    return render(request, "google_login/login.html")


def user_logout(request):
    logout(request)
    return redirect('/login')
