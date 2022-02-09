from django.contrib import admin
from .models import Products, Vendor, Category, ProductImage
# Register your models here.


from .models import ProductImage
 
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
 
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = Products
 
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products)
admin.site.register(Vendor)
admin.site.register(Category)