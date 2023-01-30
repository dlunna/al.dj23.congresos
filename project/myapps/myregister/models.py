from django.db import models

# Create your models here.

class MyRegisterModel(models.Model):
    # se agrega el verbose name para cambiar el nombre a español en el panel de admon
    name = models.CharField(max_length=50, verbose_name= "name")
    lastname = models.CharField(max_length=50, verbose_name= "lastname")
    institution = models.CharField(max_length=80, verbose_name= "institution")
    #position = models.CharField(max_length=80, verbose_name= "position")    
    emailpersonal = models.EmailField(max_length=40, verbose_name= "emailpersonal", null=True, blank=True)
    emailwork = models.EmailField(max_length=40, verbose_name= "emailwork", null=True, blank=True)
    celphone = models.CharField(max_length=50, verbose_name= "celphone", null=True, blank=True)
    grade = models.CharField(max_length=100, verbose_name= "grade", null=True, blank=True)
    snilevel = models.CharField(max_length=40, verbose_name= "snilevel", null=True, blank=True)

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
        return self.lastname