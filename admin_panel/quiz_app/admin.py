from django.contrib import admin
from .models import Question, Answer


# class AnswerInline(admin.StackedInline):
class AnswerInline(admin.TabularInline):
    model = Answer
    # extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['is_active', 'date_published', 'title']
    fieldsets = [
        (None,
         {'fields': ['title', 'is_active']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]

    inlines = [AnswerInline]

    list_display = ('title', 'date_published', 'is_active')

    # Добавим название метода модели is_popular()
    list_display = ('title', 'date_published', 'is_active', 'is_popular')

    list_filter = ['date_published']
    search_fields = ['title']
    # date_hierarchy = ['date_published']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
