from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, "home.html")

def signup(request):
    form = UserCreationForm()
    return render(request, "auth/signup.html", {'form':form})
