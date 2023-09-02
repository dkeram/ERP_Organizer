from subprocess import DETACHED_PROCESS
from unittest import result
from xml.dom.minidom import Element
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .tables import ListClient
from .models import Clients
from .forms import RegisterForm,UserForm
from django_tables2 import SingleTableView
from .autologin import AutoLogin
# Create your views here.

def main(request):
    return redirect('accounts/login/')

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        queryset = ListClient(Clients.objects.all())
        data = Clients.objects.all()
        #User choose the client and send the credential to autologin in website
        if request.method == 'POST':
            clientId = request.POST.get('clientId')
            selected_creden = Clients.objects.filter(pk__in=clientId)
            AutoLogin.auto_login(selected_creden)
    return render(request,'clients/home.html', {'table':queryset,'data':data})    

def register(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        registration_form = RegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return HttpResponseRedirect('/home/')
    return render(request,'clients/register.html',{'form':registration_form})


def new_user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    return render(request,'clients/newuser.html',{'form':form})
