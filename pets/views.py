from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pet
from .forms import PetCreateForm, PetChangeForm


class Pets(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pets.html'
    login_url = 'login'

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)


class PetDetailView(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    login_url = 'login'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Pet.objects.filter(owner=self.request.user)
        else:
            return Pet.objects.none()


class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetChangeForm
    template_name = 'pet_edit.html'
    login_url = 'login'


class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('pets')
    login_url = 'login'


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = 'pet_new.html'
    form_class = PetCreateForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
