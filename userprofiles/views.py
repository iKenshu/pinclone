from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import SignUpForm, LogInForm
from .models import Profile

# Create your views here.


class SignUpView(CreateView):
    model = Profile
    form_class = SignUpForm
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('Pin:list')


class LogInView(LoginView):
    template_name = 'login.html'
    authentication_form = LogInForm


class LogOutView(LogoutView):
    pass
