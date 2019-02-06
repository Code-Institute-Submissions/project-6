from django import forms
from .models import ContactMessage, PropertyEnquire
from listings.models import Listing


class ContactForm(forms.ModelForm):

    """ 
    Users messages form 
    """

    class Meta:
        model = ContactMessage
        fields = ['enquire', 'username', 'email', 'message']


class EnquiryForm(forms.ModelForm):

    """ 
    Users Enquiries form 
    """

    class Meta:
        model = PropertyEnquire
        fields = ['message']
