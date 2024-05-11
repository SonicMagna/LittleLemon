from django.contrib import admin
from .models import MenuItem
from .models import Reservation


# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Reservation)