from django.shortcuts import render, redirect
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
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        return redirect('/')

class LogInView(LoginView):
    template_name = 'login.html'
    authentication_form = LogInForm

class LogOutView(LogoutView):
    pass
