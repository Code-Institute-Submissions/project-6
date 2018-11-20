from django.shortcuts import render
from django.core.paginator import Paginator
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

from listings.models import Listing
from enquiries.forms import ContactForm


def index(request):
    """ 
    View for index.html (landing page)

    """
    contact_form = ContactForm()
    listings = Listing.objects.all().order_by("-list_date")[:3]

    args = {
        "listings": listings,
        "form": contact_form,
        "page_title": "Something Something",
    }
    # The contact form is submited
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, "Thank you for your message!")
            return redirect('/#contact-us', args)

    return render(request, "index.html", args)
