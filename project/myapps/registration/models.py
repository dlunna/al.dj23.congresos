from pyexpat import model
from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    # se agrega el verbose name para cambiar el nombre a español en el panel de admon
    nombre = models.CharField(max_length=40, verbose_name= "nombre")
    paterno = models.CharField(max_length=40, verbose_name= "paterno")
    materno = models.CharField(max_length=40, verbose_name= "materno")
    universidad = models.CharField(max_length=80, verbose_name= "universidad")
    celular = models.CharField(max_length=80, verbose_name= "celular")
    correo = models.EmailField(max_length=40, verbose_name= "correo")

    #Añade automaticamente la Fecha de creacion
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    #Añade la fecha de cuando de actualiza
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        #Nombre para singular de la clase en el admin
        verbose_name = "registro"
        #Nombre para plural de la clase
        verbose_name_plural = "registros"
        # Ordena los proyectos desde el ultimo creado
        ordering = ["-created"]

    # En el panel de admin
    # en lugar del nombre raro que muestre el titulo
    def __str__(self):
        return self.paterno