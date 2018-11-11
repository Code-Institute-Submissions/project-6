from django.contrib import admin

from .models import UserProfile


class UserAdminFields(admin.ModelAdmin):
    list_display = ("user",  "phone", "is_seller", "joined")
    list_editable = ("is_seller",)


admin.site.register(UserProfile, UserAdminFields)
