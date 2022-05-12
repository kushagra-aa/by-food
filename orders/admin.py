from django.contrib import admin
from .models import Order

admin.site.site_header = "By Foods"
# Register your models here.
admin.site.register(Order)
