from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.ArmedConflict)
admin.site.register(models.Medals)
