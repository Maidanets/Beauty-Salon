from django.contrib import admin
from django.urls import path
import User.views

urlpatterns = [
    path('user/', User.views.user_page),
    path('registration/', User.views.registration),
    path('login/', User.views.login),
    path('logout/', User.views.logout),
]
