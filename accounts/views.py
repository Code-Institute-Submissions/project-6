from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import UserProfileForm, UserLoginForm, EditProfileForm, EditUserForm
from listings.models import Listing


registration_email_template_id = 'd-8b80903e95924b7ba02d945ff0d8adf9'


def register(request):
    """
    User Registration view
    """

    if request.user.is_authenticated:
        messages.error(request, "You are registered and logged in already!")
        return redirect('index')
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=request.POST.get('email'))
            # Create new profile for the user
            profile = UserProfile(
                user=user,
                img=request.POST.get('img'),
                phone=request.POST.get('phone'),
                description=request.POST.get('description'),
                terms=True,
            )
            profile.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(
                    request, "You have successfully registered and logged in")
                mail = EmailMultiAlternatives(
                    subject="Registration",
                    body="Thank you",
                    from_email="The Key Keepers <admin@keykeppers.com>",
                    to=[f"{user.email}"],
                    headers={"Reply-To": "support@keykeppers.com"}
                )
                mail.template_id = registration_email_template_id
                mail.send()
                messages.success(
                    request, "Confirmation email has been sent to you.")
                return redirect('profile')
            else:
                messages.error(request, "Unable to log you in!")
        else:
            messages.error(request, "Please fix errors to continue!")
    else:
        form = UserProfileForm()
    return render(request, "register.html", {'form': form})


def login(request):
    """
    User Log-in view
    """
    # Check if user is already log in first
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in!")
        return redirect('index')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                nexturl = request.POST.get('next')
                if nexturl:
                    return redirect(nexturl)
                else:
                    return redirect('profile')
            else:
                form.add_error(
                    None, "Your username and password is incorrect!")

                return render(request, "login.html", {'form': form})
        else:
            messages.error(request, form.errors)
            return render(request, "login.html", {'form': form})
    else:
        form = UserLoginForm()
    return render(request, "login.html", {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('index')


@login_required
def profile(request):
    """
    User Profile view
    """

    user = get_object_or_404(User, pk=request.user.id)
    user_profile = get_object_or_404(UserProfile, user=user.id)
    listings = Listing.objects.all().filter(seller=user.id).order_by('-list_date')

    args = {
        "listings": listings,
        "user": user,
        "user_profile": user_profile
    }
    return render(request, "profile.html", args)


@login_required
def edit_profile(request):
    """
    View to let user to edit his profile data
    """
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(
            request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.userprofile)
    args = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "edit_profile.html", args)
