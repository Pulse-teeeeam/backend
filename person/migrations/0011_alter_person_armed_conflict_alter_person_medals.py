# Generated by Django 5.1.6 on 2025-02-15 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_person_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='armed_conflict',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.armedconflict', verbose_name='Конфликт'),
        ),
        migrations.AlterField(
            model_name='person',
            name='medals',
            field=models.ManyToManyField(blank=True, to='person.medals', verbose_name='Награды'),
        ),
    ]
