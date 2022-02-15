from django.contrib import admin
from .models import  Vendor, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Vendor)
