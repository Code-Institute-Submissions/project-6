from django.shortcuts import render

def house(request):
	""" 
	Main route for all plants
	"""
	return render(request, 'house.html')


def houses(request):
	""" 
	Main route for a single plant
	"""
	return render(request, 'houses.html')

def search(request):
	""" 
	Main route for a single plant
	"""
	return render(request, 'search.html')