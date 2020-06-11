from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from users_app.models import User
from companies_app.models import Company
import random
from random import randrange


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.filter(is_superuser=False).delete()

        count = 50
        for i in range(count):
            p = (i/count)*100
            print(f'{i}) {p} %')
            user = mixer.blend(User)
            print("id = ", user.id, user.email, user.companies)

            companies = Company.objects.all()

            # change 3 to how many random items you want
            # random_items = random.sample(items, 3)
            # if you want only a single random item


            random_1 = randrange(5)
            for each in range(random_1):
                random_company = random.choice(companies)
                # random_items = random.sample(companies, 3)
                # print(random_items)

                company_id = Company.objects.get(name=random_company).id
                print(random_company, ' ', company_id)
                user.companies.add(company_id)
                user.save()

        print('end')
