from django.contrib import admin

from myapp.forms import Records
from .models import *
# Register your models here.
admin.site.register(Item)
admin.site.register(record)
