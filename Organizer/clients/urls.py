from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ViewList.as_view()),
    path('', views.main),
    path('register/',views.register),
    path('newuser/',views.new_user),
    

]