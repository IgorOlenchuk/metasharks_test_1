from django.contrib import admin

from .models import Color, Model, Brand, Order


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('model',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'color', 'car', 'amount')