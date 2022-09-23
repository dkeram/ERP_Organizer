from subprocess import DETACHED_PROCESS
from unittest import result
from xml.dom.minidom import Element
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .tables import ListClient
from .models import Clients
from .forms import RegisterForm,UserForm
from django_tables2 import SingleTableView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
# Create your views here.

def main(request):
    return redirect('accounts/login/')

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        queryset = ListClient(Clients.objects.all())
        data = Clients.objects.all()
        if request.method == 'POST':
            clientId = request.POST.get('clientId')
            #print(clientId)
            selected_creden = Clients.objects.filter(pk__in=clientId)
            for i in selected_creden:
                onoma=i.user_name
                kodikos=i.password
                edge_options = Options()
                edge_options.add_experimental_option("detach", True)
                driver=webdriver.Edge(r"C:\Users\User\Documents\pske_system\Organizer\Organizer\msedgedriver.exe",options=edge_options)
                # driver.maximize_window()
                driver.get("https://www.ependyseis.gr/mis/(S(towin1m0zsp4ner5yxb5ofdw))/System/Login.aspx?ReturnUrl=%2fmis%2f")
                username_input_box=driver.find_element(By.NAME,"LoginControl1$txtLoginName")
                password_input_box=driver.find_element(By.NAME,"LoginControl1$txtPassword")
                login_button=driver.find_element(By.NAME,"LoginControl1$btnLogin")
                username_input_box.send_keys(onoma)
                time.sleep(0.5)
                password_input_box.send_keys(kodikos)
                time.sleep(0.5)
                login_button.click()
                return HttpResponse("{'status':'ok'}")
                
                #time.sleep(9000)
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

#def edit_client(request,client_id):
    return render(request, )