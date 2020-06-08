from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from companies_app.models import Company
from users_app.models import User
from django.utils.timezone import now


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Survey(MPTTModel):
    name = models.CharField(max_length=64)
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    link = models.CharField(max_length=128, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    hello_title = models.CharField(max_length=32, null=True, blank=True, verbose_name='ЗАГОЛОВОК')
    hello_text = models.TextField(max_length=128, null=True, blank=True, verbose_name='ТЕКСТ')
    info_title = models.CharField(max_length=32, null=True, blank=True, verbose_name='ЗАГОЛОВОК')
    info_text = models.TextField(max_length=128, null=True, blank=True, verbose_name='ТЕКСТ')
    bye_title = models.CharField(max_length=32, null=True, blank=True, verbose_name='ЗАГОЛОВОК')
    bye_text = models.TextField(max_length=128, null=True, blank=True, verbose_name='ТЕКСТ')
    created_day = models.DateField(default=now)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    contacts = models.TextField(max_length=128, null=True, blank=True)
    answers_counter = models.PositiveIntegerField(null=True, blank=True)
    language = models.ManyToManyField(Language, blank=True,  default='1')
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


class Pages(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=32,  blank=True)
    page_help = models.TextField(max_length=128, blank=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class QuestionType(models.Model):
    question_type_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'типы вопросов'

    def __str__(self):
        return self.question_type_name


class Question(MPTTModel):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=128, null=True, blank=True)
    question_help = models.TextField(max_length=128, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='question_image')
    page = models.ForeignKey(Pages, on_delete=models.CASCADE, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.question_type


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
