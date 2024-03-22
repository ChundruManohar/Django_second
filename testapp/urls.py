from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('abouts-us/',views.about,name='abouts-us'),
    path('contact-us/',views.contact,name='contact-us'),
]
