from django.db import models

class ArmedConflict(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название военного конфликта')

class Person(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=255, verbose_name='Место рождения')
    military_commissariat = models.CharField(max_length=255, verbose_name='Наименование военного комиссариата')
    military_rank = models.CharField(max_length=100, verbose_name='Воинское звание')
    conflicts_participated = models.ManyToManyField(ArmedConflict)
    awards = models.TextField(verbose_name='Награды')
    date_of_death = models.DateField(verbose_name='Дата гибели или смерти')
    burial_place = models.CharField(max_length=255, verbose_name='Место захоронения')
    biography_facts = models.TextField(verbose_name='Иные факты биографии', blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    class Meta:
        verbose_name = 'Боец'
        verbose_name_plural = 'Бойцы'