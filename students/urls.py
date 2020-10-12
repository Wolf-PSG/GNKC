from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='list'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.logout, name='dashboard')
    # path('list', views.list, name='list'),
    # path('<int:entityID>', views.single, name='entity'),
    # path('api/<name>', EntityViewSet.as_view({'get': 'retrieve'})),
    # path('api/<entityID>', EntityViewSet.as_view({'get': 'retrieve'})),
    # path('api/<origin>', EntityViewSet.as_view({'get': 'filter'})),
]