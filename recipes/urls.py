from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='root'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('auth/signup', views.signup, name='signup'),
    path('auth/login', views.login_view, name='login'),
    path('auth/logout', views.log_out, name='logout'),
]
