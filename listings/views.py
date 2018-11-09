from django.shortcuts import render
from listings.models import Listing

def house(request):
    """ 
	Main route for a single house	
	"""
    return render(request, "house.html")


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

