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
        fields = ('__all__')

class ColorOrderSerializer(serializers.ModelSerializer):
    amount = serializers.StringRelatedField(read_only=True)
    color = serializers.StringRelatedField(read_only=True)
    # color = ColorSerializer()
    class Meta:
        model = Order
        fields = ['color', 'amount']


class BrandOrderSerializer(serializers.ModelSerializer):
    amount = serializers.StringRelatedField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Order
        fields = ['brand', 'amount']
