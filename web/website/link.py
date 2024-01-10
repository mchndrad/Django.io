from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def viewbali(request):
    return render(request, "viewbali.html")

def viewbndung(request):
    return render(request, "viewbndung.html")

def viewcrbon(request):
    return render(request, "viewcrbon.html")

def viewjkrta(request):
    return render(request, "viewjkrta.html")

def viewjogja(request):
    return render(request, "viewjogja.html")

def viewmalang(request):
    return render(request, "viewmalang.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")
