from django.contrib import admin
from .models import Products, Category, ProductImage, Vendor
# Register your models here.
 
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

#admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Vendor)