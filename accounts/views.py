from django.shortcuts import render, redirect, reverse
from .forms import UserProfileForm, UserLoginForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


from django.core.exceptions import ValidationError
from django import forms


def register(request):
    """
    User Registration view
    """

    if request.user.is_authenticated:
        return redirect(reverse('index'))
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
                raise forms.ValidationError("You must accept the terms")
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
            messages.error(request, form.errors)
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
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))


@login_required
def profile(request):
    """ 
    User Profile view
    """
    return render(request, "profile.html")
