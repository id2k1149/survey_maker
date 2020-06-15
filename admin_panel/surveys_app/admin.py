from django.contrib import admin
from surveys_app.models import Question, Answer, Survey, Page, Language
from surveys_app.models import Response
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Survey)
admin.site.register(Language)
admin.site.register(Page)
admin.site.register(Question, MPTTModelAdmin)
admin.site.register(Answer)
admin.site.register(Response)
