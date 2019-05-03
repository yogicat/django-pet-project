from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard.html"
    login_url = 'login'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context


class DashboardUpdateView(LoginRequiredMixin,  UpdateView):
    model = CustomUser
    template_name = 'dashboard_edit.html'
    login_url = 'login'
