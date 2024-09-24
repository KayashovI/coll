from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.template.context_processors import request

from . import forms

from django.contrib.auth import logout
from django.shortcuts import redirect

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            print('Все не правильно')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login/login.html')


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = forms.RegisterForm()
        return render(request, 'login/register.html', {
            'form': form
        })

    if request.method =="POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")

        else:
            return render(request,'login/register.html',{
                'form':form
            })


def logout_view(request):
    logout(request)
    return redirect('/')  # Переход на страницу выхода
