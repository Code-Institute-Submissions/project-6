from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from listings.views import house
from .forms import EnquiryForm, ContactForm
from .models import PropertyEnquire
from .create_conversations import CreateConversations


def send_contact_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, "Thank you for your message!")
            return redirect('/#contact-us')
    else:
        return redirect('index')


@login_required
def send_enquire(request, user_id, house_id):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your enquire has been send.")
            return house(request, house_id)
        else:
            messages.error(request, form.errors)
            return house(request, house_id)
    else:
        return redirect('index')


@login_required
def get_messages(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            conversations = CreateConversations(request.session['_auth_user_id']).create_conversations()
            return JsonResponse(conversations, safe=False)
        else:
            return redirect('index')
    else:
        return redirect('index')


@login_required
def delete_message(request, user_id, message_id):
    if request.method == "POST":
        if user_id is not int(request.session['_auth_user_id']):
            return HttpResponse("You are not allowed to delete this message!")
        message = PropertyEnquire.objects.filter(
            pk=int(message_id), to_id=user_id)
        messages_ids = request.POST.getlist('ids[]')
        if message:
            data = serializers.serialize('json', message)
            # message.delete()
            return HttpResponse(data)
        else:
            return HttpResponse("You are not allowed to delete this message!")
    else:
        return redirect('index')


@login_required
def toggle_read(request, user_id, message_id):
    if request.method == "POST":
        message = PropertyEnquire.objects.filter(
            pk=int(message_id), to_id=user_id)
        messages_ids = request.POST.getlist('ids[]')
        for m_id in message_id:
        	messages_ids = request.POST.getlist('ids[]')
        messages_ids = request.POST.getlist('ids[]')
        messages_ids = request.POST.getlist('ids[]')
        if message:
            data = serializers.serialize('json', message)
            # message.delete()
            return HttpResponse(data)
        else:
            return HttpResponse("There seems to be a problem updating your message!")
    else:
        return redirect('index')



