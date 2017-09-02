from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Pin
from .forms import PinCreateForm

# Create your views here.
class PinList(ListView):
    model = Pin

class PinDetail(DetailView):
    model = Pin

class PinCreate(CreateView):
    model = Pin
    form_class = PinCreateForm
    template_name = 'pins/pin_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('Pin:pin_list')

class PinDelete(DeleteView):
    model = Pin
    success_url = reverse_lazy('Pin:pin_list')

class PinEdit(UpdateView):
    model = Pin
    form_class = PinCreateForm
    template_name = 'pins/pin_edit.html'

    def get_success_url(self):
        return reverse_lazy('Pin:pin_detail', args=(self.object.id, ))


