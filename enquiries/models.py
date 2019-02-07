from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from listings.models import Listing


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
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=2000)
    posted = models.DateField(default=datetime.now)
    new_message = models.BooleanField(default=True)

    def __str__(self):
        return self.enquire


class PropertyEnquire(models.Model):

    """ 
    Model for house enquire message from the user
    """

    username = models.CharField(max_length=100)
    user_id = models.IntegerField(default=1)
    house = models.ForeignKey(Listing, on_delete=models.DO_NOTHING, default=1)
    viewing = models.BooleanField(default=False)
    message = models.TextField(max_length=2000)
    posted = models.DateField(default=datetime.now)
    new_message = models.BooleanField(default=True)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.message



