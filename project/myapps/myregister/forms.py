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
    emailwork= forms.EmailField(label="Correo electronico institucional", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su correo institucional'}
    ))
    emailpersonal= forms.EmailField(label="Correo electrónico personal", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su correo personal'}
    ))
    celphone= forms.CharField(label="Contacto", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escriba su número telefónico de contacto'}
    ), min_length=10, max_length=50 )
    grade= forms.CharField(label="Grado", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe su grado académico'}
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
            'emailpersonal', 
            'emailwork', 
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