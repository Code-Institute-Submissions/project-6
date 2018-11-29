from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    """ 
    Users Enquiries form 
    """

    class Meta:
        model = ContactMessage
        fields = ['enquire', 'name', 'email', 'message']
