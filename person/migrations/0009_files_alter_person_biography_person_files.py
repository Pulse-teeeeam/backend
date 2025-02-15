# Generated by Django 5.1.6 on 2025-02-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_rename_biography_facts_person_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files', verbose_name='Файлы')),
                ('title', models.CharField(max_length=100, verbose_name='Название файла')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='person',
            name='files',
            field=models.ManyToManyField(blank=True, to='person.files', verbose_name='Доп. файлы'),
        ),
    ]
