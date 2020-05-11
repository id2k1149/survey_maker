from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from users_app.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(null=True, blank=True, upload_to='company_logo')
    employees = models.ManyToManyField(User, blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'компании'

    def __str__(self):
        return self.name


class Structure(MPTTModel):
    company = models.ManyToManyField(Company)
    department = models.CharField(max_length=64, unique=True)
    head_of_department = models.CharField(max_length=64, null=True, blank=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    workers = models.PositiveIntegerField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Структура'
        verbose_name_plural = 'Структуры'

    class MPTTMeta:
        order_insertion_by = ['department']

    def __str__(self):
        return self.department
