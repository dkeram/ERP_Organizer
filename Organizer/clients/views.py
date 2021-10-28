from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Clients
from .forms import RegisterForm,UserForm


# Create your views here.

def main(request):
    return redirect('accounts/login/')


def home(request):
    clients = Clients.objects.all()
    num = {"client_number" : clients }
    return render(request,'clients/home.html',num)


def register(request):
    registration_form = RegisterForm(request.POST)
    if registration_form.is_valid():
        registration_form.save()
        return HttpResponseRedirect('/home/')
    return render(request,'clients/register.html',{'form':registration_form})


def new_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/home/')
    return render(request,'clients/newuser.html',{'form':form})