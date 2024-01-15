from django.shortcuts import render

def home(request):
    return render(request, "loginapp/index.html")

def register(request):
    return render(request, "loginapp/register.html")


def my_login(request):
    return render(request, "loginapp/my-login.html")


def dashboard(request):
    return render(request, "loginapp/dashboard.html")
