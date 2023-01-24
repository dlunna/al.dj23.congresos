from django import forms

class CapturaForm(forms.Form):
    #widget extiende las propiedades de la etiqueta
    name= forms.CharField(label="Nombre", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ))
    father= forms.CharField(label="Paterno", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu apellido paterno'}
    ))
    mother= forms.CharField(label="Materno", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu Apellido materno'}
    ))
    university = forms.CharField(label="Universidad", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu universidad de procedencia'}
    ))
    celphone= forms.CharField(label="Celular", required= True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu número de celular'}
    ), min_length=10, max_length=50)
    email= forms.EmailField(label="Correo", required= True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escrone ti dirección de correo electrónico'}
    ), min_length=10, max_length=50)
    