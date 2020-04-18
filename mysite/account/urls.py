from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_now, name='login_now'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutme, name='logoutme'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('orders/', views.orders, name='orders'),
    path('edit/', views.edit, name='edit'),
    path('save/', views.save, name='save'),
]
