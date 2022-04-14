from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from stores.models import Products, Category, ProductImage, Vendor, Services
=======
from stores.models import Products, Category, ProductImage, Vendor, Services
#vendor_api serializers
>>>>>>> test

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Services
        fields = '__all__'


<<<<<<< HEAD
=======
 

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Services
        fields = '__all__'

>>>>>>> test
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Vendor
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'