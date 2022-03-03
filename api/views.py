from rest_framework import viewsets
#from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from stores.models import Vendor, Category, Products, ProductImage, Services
from .serializers import VendorSerializer,ProductSerializer, CategorySerializer, ProductImageSerializer, ServiceSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response  
from rest_framework import permissions


class ServiceViewSet(viewsets.ModelViewSet):
        queryset = Services.objects.all()
        serializer_class = ServiceSerializer

class VendorViewSet(viewsets.ModelViewSet):
        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet): # new permission_classes = (IsAuthorOrReadOnly,) 
        queryset = ProductImage.objects.all() 
        serializer_class = ProductImageSerializer
