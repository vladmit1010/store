from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def signup_user(request):
    '''Реєстрація нового користуача'''
    if request.method == 'GET':
        return render(request, 'katalog/signup_user.html', {'form': UserCreationForm()})
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('katalog')
            except IntegrityError:
                return render(request, 'katalog/signup_user.html',
                              {'form': UserCreationForm(), 'error': 'This username already been taken'})
        else:
            return render(request, 'katalog/signup_user.html',
                          {'form': UserCreationForm(), 'error': 'password did not match'})


def logout_user(request):
    '''Вихід зі свого аккаунта'''
    if request.method == "POST":
        logout(request)
        return redirect('katalog')


def login_user(request):
    '''Вхід да свого аккаунту'''
    if request.method == 'GET':
        return render(request, 'katalog/login.html', {'form': AuthenticationForm()})
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'katalog/login.html',
                          {'form': AuthenticationForm(), 'error': 'username or password did not match'})
        else:
            login(request, user)
            return redirect('katalog')
