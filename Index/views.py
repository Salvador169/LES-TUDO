from django.shortcuts import render

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    )

class WelcomeView(TemplateView):
    template_name = "welcome_screen.html"
