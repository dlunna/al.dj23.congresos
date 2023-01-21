from django.contrib import admin

# Register your models here.

from .models import RegisterModel

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('paterno', 'materno', 'nombre')

admin.site.register(RegisterModel, RegisterAdmin)
