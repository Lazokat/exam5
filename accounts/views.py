from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect
def register(response):
    try:
        if response.method == "POST":
            form= RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    except:
            form = RegisterForm()
            return render(response, "registration/signup.html", {'form':form})