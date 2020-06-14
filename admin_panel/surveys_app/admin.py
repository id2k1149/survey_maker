from django.contrib import admin
from surveys_app.models import Question, Answer
from surveys_app.models import Survey, Pages, Language, ReturnCode
from surveys_app.models import MonoResponse, PolyResponse
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Survey, MPTTModelAdmin)
admin.site.register(Language)
admin.site.register(ReturnCode)
admin.site.register(Pages)
admin.site.register(Question, MPTTModelAdmin)
admin.site.register(Answer)
admin.site.register(MonoResponse)
admin.site.register(PolyResponse)






