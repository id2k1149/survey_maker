from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from companies_app.models import Company
from users_app.models import User


# Create your models here.
class QuestionType(models.Model):
    question_type_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'типы вопросов'

    def __str__(self):
        return self.question_type_name


class Answer(models.Model):
    name = models.CharField(max_length=64)
    answer_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    active_answer = models.BooleanField(default=False)
    radio_buttons = models.BooleanField(default=False)
    drop_down_list = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return self.name


class Question(MPTTModel):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=128, null=True, blank=True)
    question_help = models.TextField(max_length=128, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='question_image')
    answer = models.ManyToManyField(Answer, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.question_type


class Page(models.Model):
    page_number = models.PositiveIntegerField(null=True, blank=True)
    question = models.ManyToManyField(Question, blank=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Language(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class StatusType(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Survey(MPTTModel):
    name = models.CharField(max_length=64)
    status = models.ForeignKey(StatusType, on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(max_length=128, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    contacts = models.TextField(max_length=128, null=True, blank=True)
    page = models.ManyToManyField(Page, blank=True)
    respond_counter = models.PositiveIntegerField(null=True, blank=True)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE, default='1')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.name


class ReturnCode(models.Model):
    return_code = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
