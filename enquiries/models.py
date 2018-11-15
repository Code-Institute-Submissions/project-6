from django.db import models

from datetime import datetime

class ContactMessage(models.Model):
	""" 
	Model for message from the user
	"""

	enquires = [
		('general_message', "General Message"),
		('property', "Property Enquire"),
		('feedback', "Feedback"),
		('other', "Anything else"),
	]

	enquire = models.CharField(max_length=50, choices=enquires, default='general_message')
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	message = models.TextField(max_length=2000)
	posted = models.DateField(default=datetime.now)

	def __str__(self):
		return self.enquire
