from django import forms
from .models import Listing

class AddListingForm(forms.ModelForm):
    """ 
    Form to create new listing 
    """

    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'square_feet', 'main_img', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'seller']

    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode')        
        if Listing.objects.filter(zipcode=zipcode):
            raise forms.ValidationError("Zipcode of the property must be unique")
        return zipcode
