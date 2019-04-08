from django.contrib import admin
from .models import *


class EnquireMessageAdminFields(admin.ModelAdmin):
    list_display = ('subject', 'your_name', 'email', 'message')
    list_display_links = ('your_name', 'message',)


class PropertyEnquireAdminFields(admin.ModelAdmin):
    list_display = ('sender', 'sender_email', 'to', 'house_name',
                    'viewing', 'delete_to', 'delete_sender', 'posted', 'message')
    list_display_links = ('sender', 'to', 'message',)


admin.site.register(ContactMessage, EnquireMessageAdminFields)
admin.site.register(PropertyEnquire, PropertyEnquireAdminFields)
