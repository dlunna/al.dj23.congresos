from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, "core/baiana.html")

def ProgramaView (request):
    return render(request, "myregister/programa.html")

