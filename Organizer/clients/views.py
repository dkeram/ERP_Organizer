from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .tables import ListClient
from .models import Clients
from .forms import RegisterForm,UserForm
from django_tables2 import SingleTableView

# Create your views here.

def main(request):
    return redirect('accounts/login/')

class ViewList(SingleTableView):
        table_class = ListClient
        username = ListClient.selection('user_name')
        passwrd = ListClient.selection('password')
        queryset = Clients.objects.all()
        template_name = 'clients/home.html'
#def home(request):
    #clients = Clients.objects.all()
    #num = {"client_number" : clients }
    #return render(request,'clients/home.html',num)    

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