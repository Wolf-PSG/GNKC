from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='list'),
    path('logout', views.logout, name='logout')
]
