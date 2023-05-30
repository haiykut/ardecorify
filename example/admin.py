from django.contrib import admin
# Re-register UserAdmin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from example.models import Furnitures
from django.contrib import admin
from example.models import Furniture1

admin.site.register(Furniture1)

# Register your models here.
