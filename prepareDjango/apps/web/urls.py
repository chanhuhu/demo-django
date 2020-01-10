from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from . import views


def home(request):
    return HttpResponse("Hello World")


urlpatterns = [
    path('', views.HomePage.as_view())
]


