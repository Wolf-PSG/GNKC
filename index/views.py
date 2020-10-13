from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404

from homework.forms import HomeworkForm
from homework.models import Homework
from students.models import Students
from teachers.models import Teacher
from quiz.models import Quiz, Question
from .emailForm import emailForm
from .enrolmentForm import enrolmentForm


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index/index.html')


def about(request):
    return render(request, 'index/about.html')


def philosophy(request):
    return render(request, 'index/philosophy.html')


def teachings(request):
    return render(request, 'index/teachings.html')


def enrolment(request):
    if request.method == 'POST':
        form = enrolmentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['termsRead'] == '1':
                messages.info(request, 'Form sent')
                print('worked')
                return render(request, 'index/index.html')
            else:
                form = enrolmentForm()
            # subject = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # send_mail(subject, (email + message), 'mythosAPI@gmail.com', ['parmjit.singh.1199@gmail.com'], fail_silently=False)
    else:
        form = enrolmentForm()
    return render(request, 'index/enrolment.html', {'form': form})


def media(request):
    return render(request, 'index/media.html')


def parental(request):
    if request.method == 'POST':
        form = emailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(subject, (email + message), 'mythosAPI@gmail.com',
                      ['parmjit.singh.1199@gmail.com'], fail_silently=False)
    else:
        form = emailForm()
    return render(request, 'index/parental.html', {'form': form})


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            print(request.user.id)
            teacher_id = Teacher.objects.select_related(
                'user').get(user=request.user.id)
            homework = Homework.objects.select_related(
                'teacher').filter(teacher=teacher_id)
            context = {
                'homework': homework
            }
            return render(request, 'dashboard/dashboard.html', context)
        else:
            print(request.user.id)

            student = get_object_or_404(Students, user_id=request.user.id)
            print(student.classes)
            homework_queryset = Homework.objects.select_related('teacher').filter(
                teacher=student.teacher)

            homework = get_list_or_404(
                Homework, classes=student.classes, level=student.level)

            context = {
                'homework': homework
            }
            return render(request, 'dashboard/dashboard.html', context)
            # student = Teacher.objects.select_related('')
    else:
        return redirect('index')


def homework(request):
    if request.user.is_authenticated & request.user.is_staff:
        if request.method == 'POST':
            teacher_id = Teacher.objects.select_related(
                'user').get(user=request.user.id)
            print(request.POST)
            form = HomeworkForm(request.POST)
            if form.is_valid():
                print(request.user.id)
                new_form = form.save(commit=False)
                new_form.teacher = teacher_id
                new_form.save()
                print('worked')
                return redirect('dashboard')
            else:
                print('error in form')
                form = HomeworkForm()
                return render(request, 'dashboard/setHomework.html', {'form': form})
        else:
            form = HomeworkForm()
            return render(request, 'dashboard/setHomework.html', {'form': form})
    else:
        return redirect('index')


def quiz(request):
    return render(request, 'quiz/quiz.html')
