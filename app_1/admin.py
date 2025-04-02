from django.contrib import admin
from app_1 import models
# Register your models here.

admin.site.register(models.Genre)
admin.site.register(models.Director)
admin.site.register(models.Film)
