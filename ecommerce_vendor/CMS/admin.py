from django.contrib import admin
from .models import PageGroup, Page, Banner, Blog, Testimonial, NewsEvent, ContactUs
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
# 	list_display = ('username', 'first_name', 'email', 'password')

# class UserGroupAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'slug', 'is_active')

admin.site.register(PageGroup)
admin.site.register(Page)
admin.site.register(Banner)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(NewsEvent)
admin.site.register(ContactUs)
# Register your models here.
