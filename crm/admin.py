from django.contrib import admin

# Register your models here.

# we will now register our first model Record:

from .models import Record

admin.site.register(Record)  # we will now see Records in the admin panel 