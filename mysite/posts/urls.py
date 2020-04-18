from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addimage/', views.add_image, name='add_image'),
    path('add/', views.add, name='add'),

]
