from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addnew/', views.addnew, name='addnew'),
    path('editor/<int:pk>/', views.editor, name='editor'),
    path('articleview/<int:pk>', views.articleview, name='articleview'),
    path('article/', views.get_article, name='article'),
    path('edit/<int:pk>/', views.edit_article, name='edit_article'),

]
