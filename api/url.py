from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductList, ProductDetails, StoreList, StoreDetail, CategoryList, CategoryDetail 


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('products/', ProductList.as_view(), name='Product_list'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='Product_detail'), 
    path('stores/', StoreList.as_view(), name='Store_list'),
    path('stores/<int:pk>/', StoreDetail.as_view(), name='Store-detail'),
]