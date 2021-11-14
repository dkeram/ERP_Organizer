from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .tables import ListClient
from .models import Clients
from .forms import RegisterForm,UserForm
from django_tables2 import SingleTableView

# Create your views here.

def main(request):
    return redirect('accounts/login/')

#class ViewList(SingleTableView):
    #table_class = ListClient
    #queryset = Clients.objects.all()
    #template_name = 'clients/home.html'
def home(request):
    queryset = ListClient(Clients.objects.all())
    if request.method == 'POST':
        pks = request.POST.getlist('selection')
        selected_creden = Clients.objects.filter(pk__in=pks)
        print (selected_creden)
    #num = {"client_number" : clients }   
    return render(request,'clients/home.html', {'table':queryset})    

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