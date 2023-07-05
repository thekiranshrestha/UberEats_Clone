from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomerUserAmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomerUserAmin)
