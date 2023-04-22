from django.contrib import admin
from django.urls import path
import Panel.views

urlpatterns = [
    path('panel/', Panel.views.panel_page),
    path('panel/booking/', Panel.views.panel_booking),
    path('panel/specialist/', Panel.views.panel_specialist),
    path('panel/specialist/<int:id_specialist>/', Panel.views.panel_specialist_id),
]
