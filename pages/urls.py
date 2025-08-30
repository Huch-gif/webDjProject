from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← главная страница
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]