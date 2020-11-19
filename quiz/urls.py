from quiz.views import delete
from django.urls import path

from . import views

urlpatterns = [
    path('<int:quizID>', views.quiz, name='quiz'),
    path('submit', views.submit, name='submit'),
    path('create', views.create, name='create'),
    path('add', views.addQuestion, name='add_Question'),
    path('delete/<int:questionID>', views.delete, name="delete"),
    path('delete/quiz/<int:quizID>', views.deleteQuiz, name="delete_Quiz"),
    path('update/<int:quizID>', views.updateQuiz, name="update_quiz"),
    path('update/question/<int:questionID>',
         views.updateQuestion, name="update_question"),
]
