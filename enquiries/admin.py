from django.contrib import admin

from .models import *

class EnquireMessageAdminFields(admin.ModelAdmin):
	list_display = ('enquire', 'username', 'email', 'message')


class PropertyEnquireAdminFields(admin.ModelAdmin):
	list_display = ('username', 'sender', 'email', 'message')
	

admin.site.register(ContactMessage, EnquireMessageAdminFields)
admin.site.register(PropertyEnquire, PropertyEnquireAdminFields)
