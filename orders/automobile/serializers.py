from rest_framework import serializers

from .models import Color, Model, Brand, Order


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['id', 'title']


class ModelSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Model
        fields = ['id', 'model', 'brand']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']


class OrderSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(read_only=True)
    car = ModelSerializer()
    amount = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'color', 'car', 'amount']
