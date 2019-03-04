from django import forms
from .models import ContactMessage, PropertyEnquire


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

    message = forms.CharField(min_length=15, widget=forms.Textarea)
    viewing = forms.BooleanField(required=False, label="I am interested to book a viewing")
    new_to = forms.BooleanField(required=False)

    class Meta:
        model = PropertyEnquire
        fields = ['to', 'to_id', 'to_email', 'house_id', 'house_name',
                  'viewing', 'message', 'sender', 'sender_id', 'sender_email', 'new_to']
