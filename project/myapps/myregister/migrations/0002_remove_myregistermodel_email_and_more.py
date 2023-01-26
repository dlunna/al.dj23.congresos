# Generated by Django 4.1.5 on 2023-01-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myregister', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myregistermodel',
            name='email',
        ),
        migrations.AddField(
            model_name='myregistermodel',
            name='emailpersonal',
            field=models.EmailField(blank=True, max_length=40, null=True, verbose_name='emailpersonal'),
        ),
        migrations.AddField(
            model_name='myregistermodel',
            name='emailwork',
            field=models.EmailField(blank=True, max_length=40, null=True, verbose_name='emailwork'),
        ),
        migrations.AddField(
            model_name='myregistermodel',
            name='grade',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='grade'),
        ),
        migrations.AddField(
            model_name='myregistermodel',
            name='snilevel',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='snilevel'),
        ),
        migrations.AlterField(
            model_name='myregistermodel',
            name='celphone',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='celphone'),
        ),
    ]
