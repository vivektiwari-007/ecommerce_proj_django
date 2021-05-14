from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from setting.models import Role

# Create your models here.
class UserGroup(models.Model):
	group_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, null=True, blank=True, default="")
	slug = models.SlugField(max_length=255, null=True, blank=True)
	is_active = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	created_by = models.IntegerField(null=True, blank=True)
	modified_by = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

def slug_generator(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = "SLUG"

# pre_save.connect(slug_generator, sender=POST)



class User(AbstractUser):
	user_id = models.AutoField(primary_key=True)
	user_group_id = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True, blank=True)
	role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
	first_name = models.CharField(max_length=255, null=True, blank=True, default="")
	last_name = models.CharField(max_length=255, null=True, blank=True, default="")
	avatar = models.ImageField(upload_to='media/', default="media/pexels-photo-2379004.jpeg")
	avatar_path = models.CharField(max_length=255, null=True, blank=True, default="")
	code = models.CharField(max_length=255, null=True, blank=True, default="")
	ip = models.CharField(max_length=255, null=True, blank=True, default="")
	address = models.CharField(max_length=255, null=True, blank=True, default="")
	phone_number = models.BigIntegerField(null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	created_by = models.IntegerField(null=True, blank=True)
	modified_by = models.IntegerField(null=True, blank=True)
	delete_flag = models.IntegerField(null=True, blank=True)


class Permission(models.Model):
	permission_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	json_permission = models.JSONField(null=True, blank=True)
