from django import forms
from .models import Listing


class AddListingForm(forms.ModelForm):
    """ 
    Form to create new listing 
    """

    class Meta:
        model = Listing
        fields = ['address', 'city', 'state',
                  'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'square_feet', 'main_img', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5']
