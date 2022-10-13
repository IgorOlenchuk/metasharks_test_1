from django.urls import include, path
from automobile.views import ColorsViewSet, ModelsViewSet, BrandsViewSet, OrdersViewSet

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('colors', ColorsViewSet)
router.register('models', ModelsViewSet)
router.register('brands', BrandsViewSet)
router.register('orders', OrdersViewSet)


urlpatterns = [
    path('', include(router.urls)),
] 