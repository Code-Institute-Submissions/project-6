from django.shortcuts import render

def plants(request):
	""" 
	Main route for all plants
	"""
	return render(request, 'plants.html')


def plant(request):
	""" 
	Main route for a single plant
	"""
	return render(request, 'plant.html')

def search(request):
	""" 
	Main route for a single plant
	"""
	return render(request, 'search.html')