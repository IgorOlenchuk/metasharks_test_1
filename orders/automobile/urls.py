from django.urls import path
from automobile.views import colors_list, models_list, brands_list, orders_list, order_detail


urlpatterns = [
    path('colors/', colors_list, name='colors_list'),
    path('models/', models_list, name='models_list'),
    path('brands/', brands_list, name='brands_list'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
]
