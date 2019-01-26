from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from listings.models import Listing
from listings.forms import AddListingForm


def house(request, house_id):
    """ 
        Main route for a single house	
        """
    house_data = get_object_or_404(Listing, pk=house_id)

    args = {
        'house': house_data,
        'page_title': house_data.title
    }
    return render(request, "house.html", args)


def houses(request):
    """ 
        Main route for all houses
        """
    listings = Listing.objects.all().filter(is_published=True)
    args = {
        "listings": listings,
        "page_title": "Key Keepers",
    }
    return render(request, "houses.html", args)


@login_required
def add_house(request, user_id):
    """ 
    Main route for adding new house listing
    """
    # Check if user want to add listing under different id
    if user_id is not int(request.session['_auth_user_id']):
        return redirect('add_house', user_id=request.session['_auth_user_id'])
    if request.method == 'POST':
        form = AddListingForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
        else:
            messages.error(request, form.errors)

    listing_form = AddListingForm

    args = {
        "form": listing_form
    }
    return render(request, "add_house.html", args)


@login_required
def edit_house(request, house_id):
    """ 
        Main route for editing house listing
        """
    pass


def search(request):
    """ 
        Main route for search
        """
    return render(request, "search.html")
