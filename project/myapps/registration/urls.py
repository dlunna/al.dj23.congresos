from unicodedata import name
from django.urls import path
from . import views as reg_views

urlpatterns = [
    path('', reg_views.captura, name="reg_captura"),
]
