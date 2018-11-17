from django.shortcuts import render, get_object_or_404
from listings.models import Listing


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
		"page_title": "Something something",
		}
    return render(request, "houses.html", args)


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
