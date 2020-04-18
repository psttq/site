from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('get/', views.get, name='get'),
    path('news/', views.news, name='news'),
    path('add/', views.add, name='add'),
    path('cart/', views.cart, name='cart'),
    path('remove/', views.remove, name='remove'),
    path('order/', views.order, name='order'),
    path('contacts/', views.contacts, name='contacts'),
    path('study/', views.study, name='study'),
    path('courses/', views.courses, name='courses'),
    path('orders/', views.orders, name='orders'),
    path('sendtext/', views.sendtext, name='sendtext'),
]
