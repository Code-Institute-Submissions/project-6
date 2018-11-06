from django.shortcuts import render

def house(request):
	""" 
	Main route for a single house	
	"""
	return render(request, 'house.html')


def houses(request):
	""" 
	Main route for all houses
	"""
	return render(request, 'houses.html')

def search(request):
	""" 
	Main route for search
	"""
	return render(request, 'search.html')