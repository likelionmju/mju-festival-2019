from django.contrib import admin
from .models import Food, Individual, Organization

# Register your models here.
admin.site.register(Food)
admin.site.register(Individual)
admin.site.register(Organization)