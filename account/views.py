from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from hashlib import md5


def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    elif request.method == 'POST':
        login = request.POST.get('login')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass_hash = md5(pass1.encode('utf-8')).hexdigest()
        
        report = dict()
        new_user = User.objects.create_user(login, email, pass_hash)
        if new_user is None:
            report['message'] = 'У реєстрації відмовлено!'
        else:
            report['message'] = 'Ви успішно зареєстровані!'

        return render(request, 'account/signup_report.html', context=report)


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
