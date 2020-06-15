from django.db import models
from companies_app.models import Company
from surveys_app.models import Survey


# Create your models here.
class Report(models.Model):
    report_name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return self.report_name
