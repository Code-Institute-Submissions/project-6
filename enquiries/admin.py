from django.contrib import admin

from .models import ContactMessage

class EnquireMessageAdminFields(admin.ModelAdmin):
	list_display = ('enquire', 'name', 'email', 'message')
	

admin.site.register(ContactMessage, EnquireMessageAdminFields)
