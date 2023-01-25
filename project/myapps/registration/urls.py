from django.urls import path
from . import views as reg_views

urlpatterns = [
    path('', reg_views.captura, name="reg_captura"),
    #path('nuevo', reg_views.captura, name="reg_nuevo"),
]
