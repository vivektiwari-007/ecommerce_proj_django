from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("category", views.CategoryDetail, name="categorydetail"),
    path("categoryadd", views.CategoryAdd, name="categoryadd"),
    path("categoryupdate/<int:category_id>", views.CategoryUpdate, name="categoryupdate"),
    path("categorydelete/<int:category_id>", views.CategoryDelete, name="categorydelete"),

    path("brand", views.BrandDetail, name="branddetail"),
    path("brandadd", views.BrandAdd, name="brandadd"),
    path("brandupdate/<int:brand_id>", views.BrandUpdate, name="brandupdate"),
    path("branddelete/<int:brand_id>", views.BrandDelete, name="branddelete"),

    path("product", views.ProductDetail, name="productdetail"),
    path("productadd", views.ProductAdd, name="productadd"),
    path("productupdate/<int:product_id>", views.ProductUpdate, name="productupdate"),
    path("productdelete/<int:product_id>", views.ProductDelete, name="productdelete"),

    path("coupon", views.CouponDetail, name="coupondetail"),
    path("couponadd", views.CouponAdd, name="couponadd"),
    path("couponupdate/<int:coupon_id>", views.CouponUpdate, name="couponupdate"),
    path("coupondelete/<int:coupon_id>", views.CouponDelete, name="coupondelete"),

    path("varientinfo", views.VarientInfo, name="varientinfo"),
]