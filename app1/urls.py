from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name = "home"),
    path('about',views.about,name = "about"),
    path('contact',views.contact,name = "contact"),
    path('services',views.services,name = "services"),
    # path('front',views.front,name = 'front'),
    path('signup',views.signup, name = 'signup'),
    path('handlelogin',views.handlelogin,name = 'handlelogin'),
    path('handlelogout',views.handlelogout,name="handlelogout"),
]