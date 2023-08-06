from django.contrib import admin
from .models import UserLogin, FormRegister

# Register your models here.
admin.site.register(UserLogin)
admin.site.register(FormRegister)