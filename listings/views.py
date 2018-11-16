from django.shortcuts import render, get_object_or_404
from listings.models import Listing


def house(request, house_id):
    """ 
        Main route for a single house	
        """
    house_data = get_object_or_404(Listing, pk=house_id)

    args = {
        'house': house_data,
    }
    return render(request, "house.html", args)


def houses(request):
    """ 
        Main route for all houses
        """
    listings = Listing.objects.all().filter(is_published=True)
    data = {"listings": listings}
    return render(request, "houses.html", data)


def search(request):
    """ 
        Main route for search
        """
    return render(request, "search.html")
