from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breed', views.breed, name='breed'),
    path('temperament', views.temperament, name='temperament'),
    path('care', views.care, name='care'),
]