from django import forms

class CapturaForm(forms.Form):
    name= forms.CharField(label="Nombre", required= True)
    father= forms.CharField(label="Paterno", required= True)
    mother= forms.CharField(label="Materno", required= True)
    university = forms.CharField(label="Universidad", required= True)
    celphone= forms.CharField(label="Celular", required= True)
    email= forms.EmailField(label="Correo", required= True)
    