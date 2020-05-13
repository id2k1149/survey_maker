from django.contrib import admin
from surveys_app.models import Question, QuestionType, Survey, Answer, Page, Language, StatusType
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(QuestionType)
admin.site.register(Answer)
admin.site.register(Page)
admin.site.register(Language)
admin.site.register(StatusType)
admin.site.register(Question, MPTTModelAdmin)
admin.site.register(Survey, MPTTModelAdmin)
