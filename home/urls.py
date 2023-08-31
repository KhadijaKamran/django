from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='Introduction'),
    path('workexperience', views.workexperience, name='Worke Eperience'),
    path('documents', views.documents, name='Documents'),
    path('contact', views.contact, name='Contact')

]