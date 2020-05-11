from django.db import models
from companies_app.models import Company


# Create your models here.
class QuestionType(models.Model):
    question_type_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'типы вопросов'

    def __str__(self):
        return self.question_type_name


class Question(models.Model):
    question_name = models.CharField(max_length=128)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.question_name


class Page(models.Model):
    greeting = models.CharField(max_length=64, null=True, blank=True)
    instruction = models.CharField(max_length=64, null=True, blank=True)
    final_page = models.CharField(max_length=64, null=True, blank=True)
    page_number = models.PositiveIntegerField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Survey(models.Model):
    name = models.CharField(max_length=64)
    company = models.ManyToManyField(Company)
    start_date = models.DateField()
    end_date = models.DateField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.name
