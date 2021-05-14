from django.contrib import admin
from .models import UserGroup, User, Permission
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'email', 'password')

class UserGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'is_active')

admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Permission)