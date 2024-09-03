from django.db import models

from django.contrib.auth.models import AbstractUser

# custom
class CUser(AbstractUser):
	email = models.EmailField(unique=True, max_length=255)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username", "first_name", "last_name"]

	prof_picture = models.ImageField(upload_to="users/prof_%Y", default="users/اصغر.jpg")
	bio = models.TextField(blank=True, max_length=500)
	phone_num = models.CharField(max_length=15, unique=True)
	date_birth = models.DateField(blank=True, null=True)
	pub_email = models.EmailField(blank=True, max_length=255)
	tel_id = models.CharField(blank=True, max_length=50)
	github_id = models.CharField(blank=True, max_length=50)
	twitt_id = models.CharField(blank=True, max_length=50)
	Youtube_id = models.CharField(blank=True, max_length=50)

	def __str__(self):
		return self.username

	class Meta:
		ordering = ('id',)