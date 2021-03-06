from django.urls import path

from . import views

urlpatterns = [
    path('webapps', views.index, name='webapps'),
    path('', views.index, name='webapps'),
    path('resumematch', views.resumematch, name='webapps_resumematch'),
    path('submit', views.submit, name='webapps_resumematch_submit'),
    path('run', views.run, name='run'),
]
