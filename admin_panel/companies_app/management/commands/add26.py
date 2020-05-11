from django.core.management.base import BaseCommand
from companies_app.models import Company
import string


class Command(BaseCommand):

    def handle(self, *args, **options):
        alphabet_string = string.ascii_uppercase
        alphabet_list = list(alphabet_string)

        for each in alphabet_list:

            new_name = 'Тест Компания ' + each
            print(new_name)
            Company.objects.create(name=new_name)

        print('end')
