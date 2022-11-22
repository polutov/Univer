from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    elif request.method == 'POST':

        return render(request, 'account/signup_report.html')


def email_confirm(request):
    return render(request, 'account/email_confirm.html')


def signin(request):
    return render(request, 'account/signin.html')


def signout(request):
    return render(request, 'account/signout.html')


def profile(request):
    return render(request, 'account/profile.html')


def pass_reset(request):
    return render(request, 'account/pass_reset.html')
