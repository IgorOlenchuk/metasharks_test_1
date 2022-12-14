from .models import Color, Model, Brand, Order
from .serializers import ColorSerializer, ModelSerializer, BrandSerializer, OrderSerializer, ColorOrderSerializer, BrandOrderSerializer
from rest_framework import viewsets, filters
from .pagination import OrdersPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum


class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related("car__brand")
    serializer_class = OrderSerializer
    pagination_class = OrdersPagination
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter)
    ordering = ('amount',)
    filterset_fields = ('car__brand', 'color')


class ColorsOrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.annotate(Sum('amount'))
    serializer_class = ColorOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('color',)


class BrandsOrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.annotate(Sum('amount'))
    serializer_class = BrandOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('car__brand',)
    