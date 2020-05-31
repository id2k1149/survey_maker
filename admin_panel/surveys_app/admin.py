from django.contrib import admin
from surveys_app.models import Question, QuestionType, Survey, Answer, NumberPages, Language, StatusType, ReturnCode
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(QuestionType)
admin.site.register(Answer)
admin.site.register(NumberPages)
admin.site.register(Language)
admin.site.register(StatusType)
admin.site.register(Question, MPTTModelAdmin)
admin.site.register(Survey, MPTTModelAdmin)
admin.site.register(ReturnCode)
