from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Idea)
class CustomToolAdmin(admin.ModelAdmin):
    pass
