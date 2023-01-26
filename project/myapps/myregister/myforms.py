from django import forms
from models import MyRegisterModel

class MyRegisterForm(forms.ModelForm):

    class Meta:
        model = MyRegisterModel
        fields = ['name', 'lastname', 'email']
        #fields = ['name', 'lastname', 'institution', 'celphone', 'email']
    