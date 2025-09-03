# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),          # список новостей
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('create/', views.news_create, name='news_create'),
]