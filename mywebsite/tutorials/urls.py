from django.urls import path

from . import views

urlpatterns = [
    path('tutorials', views.index, name='tutorials'),
    path('', views.index, name='tutorials'),
]