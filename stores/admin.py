from django.contrib import admin
from .models import Products, Vendor, Category
# Register your models here.e


admin.site.register(Products)
admin.site.register(Vendor)
admin.site.register(Category)