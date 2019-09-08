from django.contrib import admin

# Register your models here.

from .models import Round, Comp, Tournament

admin.site.register(Comp)
admin.site.register(Tournament)
admin.site.register(Round)
