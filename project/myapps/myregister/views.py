#from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
#from django.urls import reverse
from django.urls import reverse_lazy
from .models import MyRegisterModel

class MyRegisterListView(ListView):

    model = MyRegisterModel
    paginate_by = 100  # if pagination is desired

class MyRegisterDetailView(DetailView):

    model = MyRegisterModel
    #paginate_by = 100  # if pagination is desired

class MyRegisterCreateView(CreateView):
    model = MyRegisterModel
    fields = ['name', 'lastname', 'institution', 'celphone', 'email']

    success_url = reverse_lazy('myregister:list')

    #def get_success_url(self):
    #    return reverse('myregister:list')

