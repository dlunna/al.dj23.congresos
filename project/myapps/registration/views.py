from django.http import request
from django.shortcuts import render

# Create your views here .

def captura (render):
    return render(request, "core/captura.html")