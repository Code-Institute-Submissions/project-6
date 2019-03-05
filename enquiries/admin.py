from django.contrib import admin
from .models import *


class EnquireMessageAdminFields(admin.ModelAdmin):
    list_display = ('enquire', 'username', 'email', 'message')
    list_display_links = ('username', 'message',)


class PropertyEnquireAdminFields(admin.ModelAdmin):
    list_display = ('sender', 'sender_email', 'to', 'house_name',
                    'viewing', 'delete_to', 'delete_sender', 'posted', 'message')
    list_display_links = ('sender', 'to', 'message',)


admin.site.register(ContactMessage, EnquireMessageAdminFields)
admin.site.register(PropertyEnquire, PropertyEnquireAdminFields)
