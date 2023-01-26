from django.urls import path
#from . import views as reg_views
#from .views import MyRegisterModel
#from views import MyRegisterListView
from .views import MyRegisterListView, MyRegisterDetailView, MyRegisterCreateView, MyRegisterUpdateView, MyRegisterDeleteView, BotView

myregister_patterns = ([
    path('', MyRegisterListView.as_view(), name="list"),
    path('<int:pk>/', MyRegisterDetailView.as_view(), name="detail"),
    path('nuevo', MyRegisterCreateView.as_view(), name="create"),
    path('actualizar/<int:pk>/', MyRegisterUpdateView.as_view(), name="update"),
    path('borrar/<int:pk>/', MyRegisterDeleteView.as_view(), name="delete"),
    path('bot/', BotView, name="bot"),
    #path('lista', reg_views.captura, name="reg_nuevo"),
], 'myregister')