from django.urls import path

from . import views

urlpatterns = [
    path('', views.doctor, name='index'),
    path('patientSearch', views.patientSearch),
    path('getOCR', views.getOCR),
]

