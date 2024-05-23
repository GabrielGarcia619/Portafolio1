from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PerfilProfecional

class index(TemplateView):  # Se recomienda que las clases de vista tengan nombres en CamelCase
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = PerfilProfecional.objects.first()  # Asegúrate de que este sea el modelo correcto
        return context