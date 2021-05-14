from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/", null=True, blank=True)
    parent_id = models.CharField(max_length=50, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    meta_tag_title = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_discripation = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand/", null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

out_of_stock_choice = (
    ('instock','In Stock'),
    ('outstock','Out Stock')
)

tax_type_choice = (
    ('value','Value'),
    ('percentage','Percentage')
)

required_shipping_choice = (
    ('free','Free'),
    ('paid','Paid')
)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    sku = models.CharField(max_length=500, null=True, blank=True)
    product_slug = models.CharField(max_length=200, null=True, blank=True)
    page_content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    category_id = models.ManyToManyField(Category, null=True, blank=True)
    upc = models.CharField(max_length=100, null=True, blank=True)
    quentity = models.IntegerField(null=True, blank=True)
    out_of_stock = models.CharField(max_length=100, choices=out_of_stock_choice, null=True, blank=True)
    date_available = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    postal_code_verification = models.BooleanField(null=True, blank=True)
    brand_id = models.ManyToManyField(Brand, null=True, blank=True)
    related_product = models.CharField(max_length=100, null=True, blank=True)
    tax_type = models.CharField(max_length=100, choices=tax_type_choice, null=True, blank=True)
    product_cost = models.IntegerField(null=True, blank=True)
    add_product_cost = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    meta_tag_title = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_discripation = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    required_shipping = models.CharField(max_length=100, choices=required_shipping_choice, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    is_feature = models.BooleanField(default=True, null=True, blank=True)
    today_deal = models.BooleanField(default=True, null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


coupon_type_choice = (
    ('percentagediscount','Percentage Discount'),
    ('amountdiscount','Amount Discount')
)

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=100)
    coupon_description = models.TextField(blank=True, null=True)
    coupon_type = models.CharField(max_length=100, choices=coupon_type_choice, null=True, blank=True)
    coupon_value = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    day_left = models.IntegerField(null=True, blank=True)
    minimum_purchase_amount = models.IntegerField(null=True, blank=True)
    maximum_purchase_amount = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    product_id = models.ManyToManyField(Product, null=True, blank=True)
    coupon_limit_use = models.IntegerField(null=True, blank=True)
    no_of_times_use_discount = models.IntegerField(null=True, blank=True)
    coupne_code_apply_all_item_in_the_cart = models.BooleanField(null=True, blank=True)
    no_of_item_cart_apply_coupon = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.coupon_code


class ProductMultiImage(models.Model):
    productimage_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    multiimage = models.ImageField(upload_to="product_multiimage/", null=True, blank=True)


class ProductVarientInfo(models.Model):
    varientinfo_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    varientinfo_name = models.CharField(max_length=100, null=True, blank=True)
    varientinfo_image = models.ImageField(upload_to='vrientinfo_image/', null=True, blank=True)
    varientinfo_sku = models.CharField(max_length=100, null=True, blank=True)
    varientinfo_price = models.CharField(max_length=100, null=True, blank=True)
    varientinfo_barcode = models.CharField(max_length=100, null=True, blank=True)
    varientinfo_inventory = models.CharField(max_length=100, null=True, blank=True)
    varientinfo_status = models.BooleanField(null=True, blank=True)
