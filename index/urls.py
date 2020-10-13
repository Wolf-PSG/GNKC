from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('philosophy', views.philosophy, name='philosophy'),
    path('teachings', views.teachings, name='teachings'),
    path('enrolment', views.enrolment, name='enrolment'),
    path('media', views.media, name='media'),
    path('parental', views.parental, name='parental'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('homework', views.homework, name='homework'),
    path('quiz', views.quiz, name='quiz')
]
