from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def panel_page(request):
    return HttpResponse("Panel Page")


def panel_booking(request):
    return HttpResponse("Panel Booking")


def panel_specialist(request):
    return HttpResponse("Panel Specialist")


def panel_specialist_id(request, id_specialist):
    return HttpResponse(f"Panel Specialist id = {id_specialist}")
