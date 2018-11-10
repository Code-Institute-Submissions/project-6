from django.shortcuts import render
from django.core.paginator import Paginator
from listings.models import Listing


def index(request):
    """ 
	View for index.html (landing page)

	"""
    listings = Listing.objects.all().order_by("-list_date")[:3]

    data = {"listings": listings}

    return render(request, "index.html", data)

