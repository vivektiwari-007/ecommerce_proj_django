from django.db import models
import datetime

# Create your models here.
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    iso_code_1 = models.CharField(max_length=100, null=True, blank=True)
    iso_code_2 = models.CharField(max_length=100, null=True, blank=True)
    postal_code_required = models.BooleanField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True, blank=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DeliveryLocation(models.Model):
    deliverylocation_id = models.AutoField(primary_key=True)
    delivery_location = models.CharField(max_length=100)
    pincode = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.delivery_location


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='language/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True, blank=True)
    symbol_left = models.CharField(max_length=100, blank=True, null=True)
    symbol_right = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    orderstatus_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    priority = models.IntegerField(null=True, blank=True)
    select_color = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StockStatus(models.Model):
    stockstatus_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmailTemplate(models.Model):
    emailtemplate_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HomePage(models.Model):
    homepage_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image_right = models.ImageField(upload_to='homepage_image_right/', null=True, blank=True)
    image_left = models.ImageField(upload_to='homepage_image_left/', null=True, blank=True)
    subscribe_title = models.CharField(max_length=100, null=True, blank=True)
    subscribe_content = models.TextField(null=True, blank=True)
    subscribe_image = models.ImageField(upload_to='homepage_subscribe_image', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class GeneralSetting(models.Model):
    generalsetting_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    store_address = models.CharField(max_length=100, null=True, blank=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    maintenance = models.BooleanField(null=True, blank=True)
    store_logo = models.ImageField(upload_to="general_store_logo/", null=True, blank=True)
    store_email_logo = models.ImageField(upload_to="general_store_email_logo/", null=True, blank=True)
    store_invoice_logo = models.ImageField(upload_to="general_store_invoice_logo/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

select_type_choice = (
    ('radio','Radio'),
    ('select','Select')
) 

class Varient(models.Model):
    varient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    varient_value = models.CharField(max_length=100, null=True, blank=True)
    sort_order_value = models.CharField(max_length=100, null=True, blank=True)
    select_type = models.CharField(max_length=100, choices=select_type_choice, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Seo(models.Model):
    seo_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=100, null=True, blank=True)
    meta_discriptor = models.CharField(max_length=100, null=True, blank=True)
    meta_keyword = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meta_title


class Social(models.Model):
    social_id = models.AutoField(primary_key=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    youtube = models.URLField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)



