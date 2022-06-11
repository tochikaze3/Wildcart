from rest_framework import serializers
from accounts.models import My_User
from stores.models import Products, Category, ProductImage, Vendor, Services
#vendor_api serializers



class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = My_User
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Services
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Services
        fields = '__all__'

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