from django.db import models


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
    title = models.CharField(max_length=50, verbose_name='Модель')
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='brand',
        verbose_name='Марка'
    )

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'модели'

    def __str__(self):
        return self.title


class Order(models.Model):
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='color',
        verbose_name='Цвет'
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        related_name='model',
        verbose_name='Модель'
    )
    amount = models.CharField(max_length=50, verbose_name='Количество')
    time = models.DateTimeField(default=False, verbose_name='Дата') #указать дату по умолчанию - текущая

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Дата заказа {self.time}'