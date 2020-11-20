from django.urls import path

from . import views

urlpatterns = [
    path('<int:quizID>', views.quiz, name='quiz'),
    path('submit', views.submit, name='submit'),
    path('create', views.create, name='create'),
    path('add', views.addQuestion, name='add_Question'),
    path('delete/question/<int:questionID>',
         views.deleteQuestion, name="delete_Question"),
    path('delete/quiz/<int:quizID>', views.deleteQuiz, name="delete_Quiz"),
    path('update/quiz/<int:quizID>', views.updateQuiz, name="update_Quiz"),
    path('update/question/<int:questionID>',
         views.updateQuestion, name="update_Question"),
]
