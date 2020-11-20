from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Homework

# Create your views here.


def delete_Homework(request, homeworkID):
    if (request.user.is_authenticated & request.user.is_staff):
        try:
            homework = get_object_or_404(Homework, id=homeworkID)
            homework.delete()
            return redirect('dashboard')
        except Http404:
            print('no homework found')
            return redirect('dashboard')
