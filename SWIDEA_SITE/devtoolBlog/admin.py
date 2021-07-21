from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Devtool)
class CustomToolAdmin(admin.ModelAdmin):
    pass
