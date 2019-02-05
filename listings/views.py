from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import stripe
from listings.models import Listing
from listings.forms import AddListingForm, PayFeeForm, EditListingForm

stripe.api_key = settings.STRIPE_SECRET


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

    if request.session.get('new_house'):
                #
                # Will change it later. For now temporary remove the listing
                #
        zipcode = request.session['new_house']['zipcode'].lower()
        zipcode = zipcode.replace(" ", "")
        Listing.objects.filter(zipcode=zipcode).delete()
    # Check if user want to add listing under different id
    if user_id is not int(request.session['_auth_user_id']):
        return redirect('add_house', user_id=request.session['_auth_user_id'])
    if request.method == 'POST':
        form = AddListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_house = form.save(commit=False)
            new_house.save()
            # Store houses to session
            request.session['new_house'] = form.data
            return redirect("preview_house", user_id=user_id, house_id=new_house.id)
        else:
            messages.error(request, form.errors)
            return render(request, "add_house.html", {'form': form})
    # Automaticaly autofill feilds if house exist in session
    if request.session.get('new_house'):
        listing_form = AddListingForm(request.session['new_house'])
    else:
        listing_form = AddListingForm

    args = {
        "form": listing_form
    }
    return render(request, "add_house.html", args)


@login_required
def preview_house(request, user_id, house_id):
    """
    View for user to confirm his listing or go back and edit it
    """
    if user_id is not int(request.session['_auth_user_id']):
        return redirect('add_house', user_id=request.session['_auth_user_id'])

    house_data = get_object_or_404(Listing, pk=int(house_id))

    args = {
        'house': house_data,
        'page_title': house_data.title
    }
    return render(request, "preview_house.html", args)


@login_required
def pay_fee(request, user_id, house_id):
    """
    View for user to pay fee for new listing
    """

    if user_id is not int(request.session['_auth_user_id']):
        return redirect('add_house', user_id=request.session['_auth_user_id'])
    house_data = get_object_or_404(Listing, pk=int(house_id))
    if request.method == "POST":
        payment_form = PayFeeForm(request.POST)
        if payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(1000),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                if request.session.get('new_house'):
                    del request.session['new_house']
                Listing.objects.filter(pk=int(house_id)).update(paid_fee=True)
                args = {
                    'house_id': house_data.id
                }
                return redirect(reverse("house", kwargs={'house_id': house_data.id}))
            else:
                messages.error(request, "Unable to take payment")

        else:
            messages.error(
                request, "We were unable to take a payment with that card!")
    args = {
        'house': house_data,
        'page_title': house_data.title,
        'form': PayFeeForm,
        'publishable': settings.STRIPE_PUBLISHABLE
    }

    return render(request, "pay_fee.html", args)


@login_required
def edit_house(request, user_id, house_id):
    """ 
        Main route for editing house listing
        """
    if user_id is not int(request.session['_auth_user_id']):
        messages.error(request, "You are not allowed to edit the listing!")
        return redirect('index')
    house_data = get_object_or_404(Listing, pk=house_id)
    if request.method == "POST":
        edit_house_form = EditListingForm(
            request.POST, request.FILES, instance=house_data)
        if edit_house_form.is_valid():
            if Listing.objects.filter(zipcode=house_data.zipcode).exclude(seller_id=user_id):
                messages.error(request, "That zipcode is in use already!")
            else:
                edit_house_form.save()
                messages.success(request, "Successfully updated your listing!")
                return redirect(reverse("house", kwargs={'house_id': house_data.id}))
    house_data = house_data.__dict__
    args = {
        'form': EditListingForm(house_data),
        'house': house_data
    }

    return render(request, "edit_house.html", args)


def search(request):
    """ 
        Main route for search
        """
    return render(request, "search.html")
