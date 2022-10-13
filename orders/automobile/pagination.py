from rest_framework.pagination import PageNumberPagination

class OrdersPagination(PageNumberPagination):
    page_size = 10 
