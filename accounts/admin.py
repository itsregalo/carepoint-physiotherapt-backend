from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'phone_number', 'is_admin', 'is_staff']
    search_fields = ['email', 'username', 'phone_number']
    readonly_fields = ['date_joined', 'last_login']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2', 'is_admin', 'is_staff')}
        ),

        ('Permissions', {'fields': ('is_admin', 'is_staff')}),
        ('Personal', {'fields': ('first_name', 'last_name')}),
    )

admin.site.register(User, CustomUserAdmin)