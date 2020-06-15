from django.db import models
from django.utils.timezone import now
from quiz_app import settings
from fontawesome_5.fields import IconField


# Create your models here.
class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateField(verbose_name="Дата создания",
                                      default=now)

    is_active = models.BooleanField(verbose_name="Активный")

    # Этот метод позволяет выявить Популярный опрос для показа в админке
    def is_popular(self):
        answers = Answer.objects.filter(question_id=self.id)
        votes_total = sum([answer.votes for answer in answers])
        return votes_total > settings.POLLS_POPULAR_VOTES_LIMIT
        # if votes_total > settings.POLLS_POPULAR_VOTES_LIMIT:
        #     img_path = settings.IMG_TRUE_PATH
        # else:
        #     img_path = settings.IMG_FALSE_PATH
        # return '<img src="{}" />'.format(img_path)

    # Описание столбца в админке
    is_popular.short_description = 'Популярный'

    # Важно указать эту настройку, чтобы django не экранировал тэги
    # is_popular.allow_tags = True

    # Вот настройка, заменяющая False/True на иконки в админке
    is_popular.boolean = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)
    icon = IconField(blank=True, null=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
