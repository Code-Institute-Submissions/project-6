from django.shortcuts import render

def index(request):
	""" 
	View for index.html (landing page)

	"""
	return render(request, 'index.html')
