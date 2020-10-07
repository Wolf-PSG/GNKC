from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .emailForm import emailForm
from .enrolmentForm import enrolmentForm

# Create your views here.
def index(request):
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
            send_mail(subject, (email + message), 'mythosAPI@gmail.com', ['parmjit.singh.1199@gmail.com'], fail_silently=False)
    else:
      form = emailForm()
    return render(request, 'index/parental.html', {'form': form})
