from django.contrib import admin
from django.urls import path
import Panel.views

urlpatterns = [
    path('', Panel.views.panel_page),
    path('booking/', Panel.views.panel_booking),
    path('services/', Panel.views.panel_services),
    path('services/<int:id_service>/', Panel.views.panel_service_id),
    path('masters/', Panel.views.panel_masters),
    path('masters/<int:id_master>/', Panel.views.panel_master_id),
]
