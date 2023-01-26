from django.contrib import admin

# Register your models here.

from .models import MyRegisterModel

class MyRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'lastname', 'emailwork')

admin.site.register(MyRegisterModel, MyRegisterAdmin)
