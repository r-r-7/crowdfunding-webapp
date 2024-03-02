from django.contrib import admin

# Register your models here.

from .models import Startup
from .models import Investor
from .models import Fundraiser

admin.site.register(Startup)
admin.site.register(Investor)
admin.site.register(Fundraiser)