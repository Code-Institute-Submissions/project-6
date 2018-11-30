from django import forms
from .models import Listing
from django.contrib.auth.models import User


class AddListingForm(forms.ModelForm):
    """ 
    Form to create new listing 
    """

    class Meta:
        model = Listing
        fields = ['title','address', 'city', 'state',
                  'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'square_feet', 'main_img', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'seller']