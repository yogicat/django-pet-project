from django.shortcuts import render
from django.views.generic import TemplateView

from pets.models import Pet


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['pets'] = Pet.objects.filter(is_main=True)
        return context
