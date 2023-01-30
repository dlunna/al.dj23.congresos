from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def root(request):
    return render(request, "core/baiana.html")

def ProgramaView (request):
    return render(request, "myregister/programa.html")

class Error404View(TemplateView):
    template_name = "core/error404.html"

