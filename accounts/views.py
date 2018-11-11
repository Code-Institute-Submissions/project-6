from django.shortcuts import render, redirect

def register(request):
	""" 
	User Register view
	"""
	return render(request, "register.html")


def login(request):
	""" 
	User Log-in view
	"""
	return render(request, "login.html")


def logout(request):
	""" 
	User Log-ou view
	"""
	return redirect(request, "index.html")


def profile(request):
	""" 
	User Profile view
	"""
	return render(request, "profile.html")
