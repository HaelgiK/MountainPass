from django.db import models


# модель пользователя
class User(models.Model):
    email = models.EmailField(max_length=64, unique=True)
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

