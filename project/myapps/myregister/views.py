#from django.shortcuts import render
from importlib import import_module
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse
from django.urls import reverse_lazy
from .models import MyRegisterModel
from .forms import MyRegisterForm

class MyRegisterListView(ListView):
    model = MyRegisterModel
    paginate_by = 100  # if pagination is desired

class MyRegisterDetailView(DetailView):
    model = MyRegisterModel
    #paginate_by = 100  # if pagination is desired

class MyRegisterCreateView(CreateView):
    model = MyRegisterModel
    form_class=MyRegisterForm    
    #fields = ['name']
    success_url = reverse_lazy('myregister:list')
    #def get_success_url(self):
    #    return reverse('myregister:list')

class MyRegisterUpdateView(UpdateView):
    model = MyRegisterModel
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('myregister:list')

class MyRegisterDeleteView(DeleteView):
    model = MyRegisterModel
    success_url = reverse_lazy('myregister:list')