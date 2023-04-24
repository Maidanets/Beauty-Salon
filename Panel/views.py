from django.http import HttpResponse
from django.shortcuts import render
from Salon.models import Services, Master, Schedule, Booking

# Create your views here.


def panel_page(request):
    return HttpResponse("Panel Page")


def panel_booking(request):
    return HttpResponse("Panel Booking")


def panel_services(request):
    if request.method == "POST":
        service = Services(
            name_service=request.POST['name_service'],
            time_service=request.POST['time_service'],
            price_service=request.POST['price_service']
        )
        service.save()
    services = Services.objects.all()
    return render(request, "panel_services.html", {'services': services})


def panel_service_id(request, id_specialist):
    return HttpResponse(f"Panel Specialist id = {id_specialist}")


def panel_masters(request):
    # [value for key, value in request.POST.items() if key.startswith('services_master')]

    if request.method == "POST":
        master = Master(
            name_master=request.POST['name_master'],
            phone_master=request.POST['phone_master'],
            rank_master=request.POST['rank_master'],
        )
        master.save()

        service_ids = [value for key, value in request.POST.items() if key.startswith('services_master')]
        for service_id in service_ids:
            service = Services.objects.get(id=service_id)
            master.services_master.add(service)
        master.save()

    masters = Master.objects.all()
    services = Services.objects.all()
    return render(request, "panel_masters.html", {'masters': masters, 'services': services})


def panel_master_id(request, id_master):
    if request.method == "POST":
        schedule = Schedule(
            master_id=id_master,
            date=request.POST['date'],
            start_work=request.POST['start_work'],
            end_work=request.POST['end_work']
        )
        schedule.save()
    current_schedule = Master.objects.get(id=id_master)
    work_schedule = Schedule.objects.filter(master_id=current_schedule).all()
    return render(request, "panel_master_one.html", {'work_schedule': work_schedule})
