from django.contrib import admin
<<<<<<< HEAD
from .models import Products, Vendor, Category
# Register your models here.e
=======
from .models import Products, Vendor, Category, ProductImage
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
>>>>>>> test

#admin.site.register(Products)
admin.site.register(Vendor)
admin.site.register(Category)