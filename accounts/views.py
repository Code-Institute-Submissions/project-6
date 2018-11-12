from django.shortcuts import render, redirect, reverse
from .forms import UserProfileForm, UserLoginForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


def register(request):
    """
    User Registration view
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # If valid save the user
            form.save()
            user = User.objects.get(email=request.POST.get('email'))
			# Check if terms are accepted
            if request.POST.get('terms'):
                terms = True
            else:
                terms = False
			# Create new profile for the user
            profile = UserProfile(
                user=user,
                img=request.POST.get('img'),
                phone=request.POST.get('phone'),
                description=request.POST.get('description'),
                terms=terms,
            )
            profile.save()
            # Log in the user
            auth.login(request, user)
            messages.success(
                request, "You have successfully registered and logged in")
            return redirect(reverse('index'))
    else:
        form = UserProfileForm()
    return render(request, "register.html", {'form': form})


def login(request):
    """ 
    User Log-in view
    """
    form = UserLoginForm()
    return render(request, "login.html", {'form': form})


@login_required
def logout(request):
    """ 
    User Log-ou view
    """
    return redirect(request, "index.html")


@login_required
def profile(request):
    """ 
    User Profile view
    """
    return render(request, "profile.html")
