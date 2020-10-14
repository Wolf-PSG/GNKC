from django.urls import path

from . import views

urlpatterns = [
    path('<int:quizID>', views.quiz, name='quiz'),
]
