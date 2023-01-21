from django.shortcuts import render
from .forms import CapturaForm

# Create your views here .

def captura (request):
    captura_form = CapturaForm()
    return render(request, "registration/captura.html", {'form':captura_form})
