from django.contrib import admin
from companies_app.models import Company
from companies_app.models import Structure
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Company)

admin.site.register(Structure, MPTTModelAdmin)
