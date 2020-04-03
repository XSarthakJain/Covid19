from django.contrib import admin

# Register your models here.
from .models import Covid
admin.site.register(Covid)

from .models import Patients
admin.site.register(Patients)