from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sort/', views.sort, name='sort'),
]
