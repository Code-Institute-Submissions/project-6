from django import forms
from .models import Listing


class AddListingForm(forms.ModelForm):
    """ 
    Form to create new listing 
    """

    bedrooms = forms.IntegerField(min_value=0,max_value=10)
    bathrooms = forms.IntegerField(min_value=0, max_value=5)
    garage = forms.IntegerField(min_value=0, max_value=5)
    bedrooms = forms.IntegerField(min_value=0,max_value=10)

    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'square_feet', 'main_img', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'seller']

    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode').lower()
        zipcode = zipcode.replace(" ", "")
        if Listing.objects.filter(zipcode=zipcode):
            raise forms.ValidationError(
                "Zipcode of the property must be unique")
        return zipcode
