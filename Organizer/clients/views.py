from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .tables import ListClient
from .models import Clients
from .forms import RegisterForm,UserForm
from django_tables2 import SingleTableView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Create your views here.

def main(request):
    return redirect('accounts/login/')

def home(request):
    queryset = ListClient(Clients.objects.all())
    if request.method == 'POST':
        pks = request.POST.get('selection')
        print(pks)
        selected_creden = Clients.objects.filter(pk__in=pks)
        for i in selected_creden:
            onoma=i.user_name
            kodikos=i.password
            print(onoma)
            print(kodikos)
            driver=webdriver.Edge(r"C:\Users\User\Documents\pske_system\Organizer\Organizer\msedgedriver.exe")
            driver.maximize_window()
            driver.get("https://www.ependyseis.gr/mis/(S(towin1m0zsp4ner5yxb5ofdw))/System/Login.aspx?ReturnUrl=%2fmis%2f")
            username_input_box=driver.find_element_by_name("LoginControl1$txtLoginName")
            password_input_box=driver.find_element_by_name("LoginControl1$txtPassword")
            login_button=driver.find_element_by_name("LoginControl1$btnLogin")
            username_input_box.send_keys(onoma)
            time.sleep(2)
            password_input_box.send_keys(kodikos)
            time.sleep(2)
            login_button.click()
            driver.open()
            
            print (selected_creden) 
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