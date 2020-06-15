from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from surveys_app.models import Survey
from companies_app.models import Company
import random
from random import randrange
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        Survey.objects.all().delete()
        fake = Faker('ru_RU')

        count = 10
        for i in range(count):
            p = (i/count)*100
            print(f'{i}) {p} %')

            new_survey = fake.sentence(4)
            date_1 = fake.date()
            date_2 = fake.date()
            hello = fake.sentence(2)
            hello_text = fake.sentence(10)
            inst = fake.sentence(1)
            inst_text = fake.sentence(6)
            bye = fake.sentence(2)
            bye_text = fake.sentence(8)
            companies = Company.objects.all()
            random_company = random.choice(companies)

            # company_id = Company.objects.get(name=random_company).id

            Survey.objects.create(name=new_survey,
                                  start_date=date_1,
                                  end_date=date_2,
                                  company=random_company,
                                  hello_title=hello,
                                  hello_text=hello_text,
                                  info_title=inst,
                                  info_text=inst_text,
                                  bye_title=bye,
                                  bye_text=bye_text,
                                  )

        print('end')
