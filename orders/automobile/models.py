from django.db import models
from django.utils import timezone


class Color(models.Model):
    title = models.CharField(max_length=50, verbose_name='Цвет')

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=50, verbose_name='Марка')

    class Meta:
        verbose_name = 'марка'
        verbose_name_plural = 'марки'

    def __str__(self):
        return self.title


class Model(models.Model):
    model = models.CharField(max_length=50, verbose_name='Модель')
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='models',
        verbose_name='Марка автомобиля'
    )
    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели'

    def __str__(self):
        return self.model


class Order(models.Model):
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Цвет'
    )
    car = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Автомобиль'
    )
    amount = models.CharField(max_length=50, verbose_name='Количество')
    order_date = models.DateTimeField(default=timezone.now, verbose_name='Дата', db_index=True)
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Дата заказа {self.order_date}'