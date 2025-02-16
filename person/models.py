from django.db import models

# TODO: Добавить другие файлы

class Files(models.Model):
    file = models.FileField(upload_to='files', verbose_name='Файлы')
    title = models.CharField(max_length=100, verbose_name='Название файла')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class ArmedConflict(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название военного конфликта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Военный конфликт'
        verbose_name_plural = 'Военные конфликты'

class Medals(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название медали')
    image = models.ImageField(upload_to="medals/", verbose_name="Изображение медали")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Медаль'
        verbose_name_plural = 'Медали'

class Person(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=255, verbose_name='Место рождения')
    military_commissariat = models.CharField(max_length=255, verbose_name='Наименование военного комиссариата')
    military_rank = models.CharField(max_length=100, verbose_name='Воинское звание')
    armed_conflict = models.ForeignKey(ArmedConflict, verbose_name='Конфликт', on_delete=models.CASCADE)
    medals = models.ManyToManyField(Medals, verbose_name='Награды', blank=True)
    date_of_death = models.DateField(verbose_name='Дата гибели или смерти')
    burial_place = models.CharField(max_length=255, verbose_name='Место захоронения')
    biography = models.TextField(verbose_name='Биография', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to="photos/", blank=True, null=True)
    files = models.ManyToManyField(Files, verbose_name='Доп. файлы', blank=True)

    public = models.BooleanField(verbose_name='Опубликовано?', default=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    class Meta:
        verbose_name = 'Боец'
        verbose_name_plural = 'Бойцы'


class Logging(models.Model):
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    EVENTS = (
        ('create', 'Создание'),
        ('edit', 'Изменение'),
    )
    event = models.CharField(max_length=10, choices=EVENTS)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event} {self.person}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'