from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Food ,Exercise
from .forms import Foodform ,Exerciseform


def index(req):
    return render(req, "myweb/index.html")

def food(req):
    foods = Food.objects.all()
    return render(req, "myweb/food.html" ,{'foods':foods})

def addfood(request):
    if request.method == 'POST':
        form = Foodform(request.POST)

        if form.is_valid():
            f = form.save()
            f.save()
            return redirect("/food")
    else:
        form = Foodform()
        context = {'form': form}
        return render(request, 'myweb/addfood.html', context)

def exercise(req):
    Exercises = Exercise.objects.all()
    return render(req, "myweb/Exercise.html" ,{'Exercises':Exercises})

def addexercise(request):
    if request.method == 'POST':
        form = Exerciseform(request.POST)

        if form.is_valid():
            f = form.save()
            f.save()
            return redirect("/Exercise")
    else:
        form = Exerciseform()
        context = {'form': form}
        return render(request, 'myweb/addExercise.html', context)

def login_user(req):
    if req.method == 'POST':
        user = User.objects.get(username=req.POST['username'])
        user = authenticate(username=user.username, password=req.POST['password'])
        if user:
            login(req, user)
            return redirect('/')

        else:
            return render(req, 'myweb/login.html')

    else:
        return render(req, 'myweb/login.html')

def logout_user(req):
    logout(req)
    return redirect('/')

def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(req, "myweb/register.html", context={"form":form})




