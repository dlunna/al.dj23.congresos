from django import forms
from .models import MyRegisterModel

class MyRegisterForm(forms.ModelForm):

    class Meta:
        model = MyRegisterModel
        fields = ['name', 'lastname', 'email']
        #fields = ['name', 'lastname', 'institution', 'celphone', 'email']
        forms.widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }