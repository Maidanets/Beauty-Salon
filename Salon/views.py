import datetime
from django.http import HttpResponse

from django.shortcuts import render
from Salon.models import Services, Master, Booking, Schedule
from django.views.generic import ListView, DetailView


# class ServicesList(ListView):
#     model = Services
#     template_name = 'services.html'
#     context_object_name = 'services'


# class ServicesDetail(DetailView):
#     model = Services
#     template_name = 'service.html'
#     context_object_name = 'service'


def salon_page(request):
    return HttpResponse("Salon Page")


def services(request):
    masters_ids = Schedule.objects.filter(
        date__gte=datetime.date.today(),
        date__lte=datetime.date.today()+datetime.timedelta(days=7)
    ).values_list('master_id', flat=True).distinct()

    available_master = Master.objects.filter(id__in=masters_ids, statys_master=True).distinct()
    available_services = Services.objects.filter(master__id__in=available_master).distinct()

    return render(request, "services.html", {'services': available_services})


def service_id(request, id_service):
    return HttpResponse(f"Service id = {id_service}")


def specialist(request):
    return HttpResponse("Specialist")


def specialist_id(request, id_specialist):
    return HttpResponse(f"Specialist id = {id_specialist}")


def booking(request):
    if request.method == "POST":
        booking_user = Booking(
            client_name=request.POST['client_name'],
            client_phone=request.POST['client_phone'],
            date_time=request.POST['date_time'],
            start_time=request.POST['start_time'],
            master_id_id=request.POST['master_id_id'],
            services_id_id=request.POST['services_id_id']
        )
        booking_user.save()
    master = Master.objects.all()
    service = Services.objects.all()
    return render(request, "booking.html", {'master': master, 'service': service})
