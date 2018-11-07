from django.db import models
from datetime import datetime

from accounts.models import User

class Listing(models.Model):
	""" 
	Model for creating a single listing (house)
	"""
	
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=20)
	description = models.TextField(blank=True)
	price = models.IntegerField()
	bedrooms = models.IntegerField()
	bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
	garage = models.IntegerField(default=0)
	square_feet = models.IntegerField()
	main_img = models.ImageField(upload_to='media/imgs/')
	img_1 = models.ImageField(upload_to='media/imgs/', blank=True)
	img_2 = models.ImageField(upload_to='media/imgs/', blank=True)
	img_3 = models.ImageField(upload_to='media/imgs/', blank=True)
	img_4 = models.ImageField(upload_to='media/imgs/', blank=True)
	img_5 = models.ImageField(upload_to='media/imgs/', blank=True)
	is_published = models.BooleanField(default=True)
	paid_fee = models.BooleanField(default=False)
	list_date = models.DateTimeField(default=datetime.now, blank=True)
	seller = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
