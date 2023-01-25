# Generated by Django 4.1.5 on 2023-01-25 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyRegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('lastname', models.CharField(max_length=40, verbose_name='lastname')),
                ('institution', models.CharField(max_length=80, verbose_name='institution')),
                ('celphone', models.CharField(max_length=80, verbose_name='celphone')),
                ('email', models.EmailField(max_length=40, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'registro',
                'verbose_name_plural': 'registros',
                'ordering': ['-created'],
            },
        ),
    ]