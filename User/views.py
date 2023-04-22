from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def user_page(request):
    return HttpResponse("User Page")


def registration(request):
    return HttpResponse("Registration page")


def login(request):
    return HttpResponse("Login page")


def logout(request):
    return HttpResponse("Logout page")
