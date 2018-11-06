from django.db import models

from datetime import datetime


class User(models.Model):
	""" 
	Model for User (seller)
	"""

	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to='media/imgs/', blank=True)
	phone = models.IntegerField()
	is_seller = models.BooleanField(default=False)
	joined = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.name
