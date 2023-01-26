from django import forms
from .models import MyRegisterModel

class MyRegisterForm(forms.ModelForm):

    class Meta:
        model = MyRegisterModel
        fields = ['name', 'lastname', 'institution', 'emailpersonal', 'emailwork', 'celphone', 'grade', 'snilevel']
        
        forms.widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'emailpersonal': forms.TextInput(attrs={'class':'form-control'}),
        }