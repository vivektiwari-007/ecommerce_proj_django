from django.contrib import admin
from .models import Category, Brand, Product, Coupon, ProductMultiImage, ProductVarientInfo
# Register your models here.


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Coupon)
admin.site.register(ProductVarientInfo)
admin.site.register(ProductMultiImage)