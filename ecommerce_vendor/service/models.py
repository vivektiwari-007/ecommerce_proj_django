from django.db import models
import datetime

# Create your models here.
class ServiceCategory(models.Model):
    servicecategory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    meta_tag_title = models.CharField(max_length=50, null=True, blank=True)
    meta_tag_description = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='servicecategory/', null=True, blank=True)
    parent_id = models.CharField(max_length=50, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ServiceList(models.Model):
    servicelist_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='servicelist/', null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    category_id = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    meta_tag_title = models.CharField(max_length=50, null=True, blank=True)
    meta_tag_description = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

