from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import My_User



class AccountAdmin(UserAdmin):
    list_display = ('email', 'mobile', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'mobile')
    readonly_fields = ('id', 'last_login', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(My_User, AccountAdmin)