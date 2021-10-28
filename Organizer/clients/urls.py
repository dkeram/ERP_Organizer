from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('', views.main),
    path('register/',views.register),
    path('newuser/',views.new_user),
    

]