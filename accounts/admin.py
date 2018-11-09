from django.contrib import admin

from .models import User


class UserAdminFields(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "is_seller", "joined")
    list_editable = ("is_seller",)


admin.site.register(User, UserAdminFields)
