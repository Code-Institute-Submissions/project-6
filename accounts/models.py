from django.db import models
from django.contrib.auth.models import User

from listings.models import Listing
from datetime import datetime


class UserProfile(models.Model):
	""" 
	Model for User (seller)
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to='media/imgs/', blank=True)
	phone = models.IntegerField()
	is_seller = models.BooleanField(default=False)
	joined = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.user.email


User.profile = property(lambda u: UserProfile.object.get_or_create(user=u)[0])