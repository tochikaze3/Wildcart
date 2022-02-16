from rest_framework import serializers
from stores.models import Products, Category, ProductImage, Vendor
#vendor_api serializers

#class UserSerializer(serializers.ModelSerializer):
    
    #class Meta:
        #model = UserProfile() 
        #fields = ('id', 'email',)

 
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