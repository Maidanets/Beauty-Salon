from django.contrib import admin
from django.urls import path
import Salon.views

urlpatterns = [
    path('', Salon.views.salon_page),
    path('services/', Salon.views.services),
    path('services/<int:id_service>/', Salon.views.service_id),
    path('specialist/', Salon.views.specialist),
    path('specialist/<int:id_specialist>/', Salon.views.specialist_id),
    path('booking/', Salon.views.booking),
]
