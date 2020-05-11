from django.contrib import admin
from surveys_app.models import Survey, Question, QuestionType
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(QuestionType)

