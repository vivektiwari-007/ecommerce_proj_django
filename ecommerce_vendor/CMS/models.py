from django.db import models
import datetime



# Create your models here.
class PageGroup(models.Model):
    page_group_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True, default="")
    intro = models.TextField(max_length=500, null=True, blank=True)
    Full_text = models.TextField(max_length=500, null=True, blank=True)
    page_group_id_id = models.ForeignKey(PageGroup, on_delete=models.CASCADE, blank=True, null=True)
    sort_order = models.IntegerField(null=True, blank=True)
    meta_tag_title = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_discripation = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    view_page_count = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    container_name = models.CharField(max_length=500, null=True, blank=True)
    view_page_count = models.IntegerField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='banner/')
    content = models.TextField(max_length=500, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/')
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    discription = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='testimonial')
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class NewsEvent(models.Model):
    newsevent_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="newsevent/")
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


day_choice = (
    ('sunday','Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday')
)

class ContactUs(models.Model):
    contactus_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    start_day = models.CharField(max_length=10, choices=day_choice, null=True, blank=True)
    end_day = models.CharField(max_length=10, choices=day_choice, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    image = models.ImageField(upload_to="contactus/", blank=True, null=True)
    map_link = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.IntegerField(null=True, blank=True)
    modified_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

