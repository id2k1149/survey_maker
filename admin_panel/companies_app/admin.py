from django.contrib import admin
from companies_app.models import Company, Department
from mptt.admin import MPTTModelAdmin


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, MPTTModelAdmin)
