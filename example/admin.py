from django.contrib import admin
# Re-register UserAdmin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from example.models import Furnitures
class FurnituresInline(admin.StackedInline):
    model = Furnitures
    can_delete = False
    verbose_name_plural = "Furnitures"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.
