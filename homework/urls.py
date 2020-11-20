from django.urls import path

from . import views

urlpatterns = [
    path('delete/<int:homeworkID>', views.delete_Homework, name='delete_homework'),
]
