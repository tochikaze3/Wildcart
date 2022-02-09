from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductList, ProductDetails, VendorList, VendorDetail, CategoryList, CategoryDetail 


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('products/', ProductList.as_view(), name='Product_list'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='Product_detail'), 
    path('Vendors/', VendorList.as_view(), name='Store_list'),
    path('Vendors/<int:pk>/', VendorDetail.as_view(), name='Store-detail'),
]