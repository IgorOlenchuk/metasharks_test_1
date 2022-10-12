from .models import Color, Model, Brand, Order
from .serializers import ColorSerializer, ModelSerializer, BrandSerializer, OrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def colors_list(request):
    colors = Color.objects.all()
    serializer = ColorSerializer(colors, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def models_list(request):
    models = Model.objects.all()
    serializer = ModelSerializer(models, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def brands_list(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def orders_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

