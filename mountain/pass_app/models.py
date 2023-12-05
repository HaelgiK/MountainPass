
from django.db import models
from django.utils import timezone

from func_path import get_image_path
from resources import LEVELS, STATUS


# модель пользователя
class User(models.Model):
    email = models.EmailField(max_length=64)
    phone = models.CharField( max_length=12, verbose_name='Телефон')
    fam = models.CharField(max_length=64, verbose_name='Фамилия')
    name = models.CharField(max_length=64, verbose_name='Имя')
    otc = models.CharField(max_length=64, verbose_name='Отчество', blank=True, null=True)

    # class Meta:
    #     constraints = [models.UniqueConstraint(fields=['email'], name="user_unique")]

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'


# модель географических координат
class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f"широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}"

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


class Level(models.Model):
    winter = models.CharField(verbose_name='Зима', choices=LEVELS, max_length=6, null=True, blank=True)
    summer = models.CharField(verbose_name='Лето', choices=LEVELS, max_length=6, null=True, blank=True)
    autumn = models.CharField(verbose_name='Осень', choices=LEVELS, max_length=6, null=True, blank=True)
    spring = models.CharField(verbose_name='Весна', choices=LEVELS, max_length=6, null=True, blank=True)

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"


class MountainPass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=8, default='NW')
    beauty_title = models.CharField(verbose_name='Название топонима', default='пер.', max_length=255)
    title = models.CharField(verbose_name='Название', blank=True, null=True, max_length=255)
    other_titles = models.CharField(verbose_name='Другое название', blank=True, null=True, max_length=255)
    connect = models.TextField(verbose_name='Что связывает', blank=True, null=True)
    add_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.pk} {self.beauty_title}'

    # class Meta:
    #     verbose_name = "Перевал"
    #     verbose_name_plural = "Перевалы"


class Image(models.Model):
    mountain_pass = models.ForeignKey(MountainPass, on_delete=models.CASCADE,
                                      related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to=get_image_path, verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)
    add_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.pk}: {self.title} {self.image}'

