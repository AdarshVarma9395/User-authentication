from django.shortcuts import render, redirect
from . forms import CreateUserForm,LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "loginapp/index.html")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("my-login")
        
    context = {"form":form}
    return render(request, "loginapp/register.html",context)


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
    context = {"loginform" : form}

    return render(request, "loginapp/my-login.html",context)



def user_logout(request):
    auth.logout(request)
    return redirect("my-login")

@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "loginapp/dashboard.html")
