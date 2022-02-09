from django.contrib import admin
from .models import Products, Vendor, Category
# Register your models here.


admin.site.register(Products)
admin.site.register(Vendor)
admin.site.register(Category)