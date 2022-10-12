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
        fields = ['id', 'title', 'brand']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'title']


class OrderSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    color = serializers.StringRelatedField(read_only=True)
    model = serializers.StringRelatedField(read_only=True)
    amount = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'color', 'model', 'brand', 'amount']
