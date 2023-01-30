from django import forms
from .models import MyRegisterModel

class MyRegisterForm(forms.ModelForm):
    
    name= forms.CharField(label="Nombre", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su nombre'}
    ))
    lastname= forms.CharField(label="Apellidos", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba sus apellidos'}
    ))
    institution= forms.CharField(label="Institución", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su institución de procedencia'}
    ))
    emailwork= forms.EmailField(label="Correo institucional", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su correo institucional'}
    ))
    emailpersonal= forms.EmailField(label="Correo personal", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su correo personal'}
    ))
    celphone= forms.CharField(label="Telefóno de contacto", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su número telefónico de contacto'}
    ), min_length=10, max_length=30 )
    
    grade= forms.CharField(label="Grados", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Grados académicos con los que cuenta'}
    ))
    snilevel= forms.CharField(label="SNI", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su nivel de SNI'}
    ))
    

    class Meta:
        model = MyRegisterModel
        fields = [
            'name', 
            'lastname', 
            'institution', 
            'emailwork', 
            'emailpersonal', 
            'celphone', 
            'grade', 
            'snilevel'
            ]
        
        widgets = {
            #'name': forms.TextInput(attrs={'class':'form-control'}),
            #'lastname': forms.TextInput(attrs={'class':'form-control'}),
            #'institution': forms.TextInput(attrs={'class':'form-control'}),
            #'emailpersonal': forms.TextInput(attrs={'class':'form-control'}),
            #'emailwork': forms.TextInput(attrs={'class':'form-control'}),
            #'celphone': forms.TextInput(attrs={'class':'form-control'}),
            #'grade': forms.TextInput(attrs={'class':'form-control'}),
            #'snilevel': forms.TextInput(attrs={'class':'form-control'})
        }