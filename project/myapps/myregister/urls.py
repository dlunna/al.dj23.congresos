from django.urls import path
#from . import views as reg_views
#from .views import MyRegisterModel
#from views import MyRegisterListView
from .views import MyRegisterListView, MyRegisterDetailView, MyRegisterCreateView, MyRegisterUpdateView, MyRegisterDeleteView, BotView

myregister_patterns = ([
    path('list', MyRegisterListView.as_view(), name="list"),
    path('', MyRegisterCreateView.as_view(), name="create"),
    path('bot/', BotView, name="bot"),
    #path('<int:pk>/', MyRegisterDetailView.as_view(), name="detail"),
    #path('actualizar/<int:pk>/', MyRegisterUpdateView.as_view(), name="update"),
    #path('borrar/<int:pk>/', MyRegisterDeleteView.as_view(), name="delete"),
    #path('lista', reg_views.captura, name="reg_nuevo"),
], 'myregister')