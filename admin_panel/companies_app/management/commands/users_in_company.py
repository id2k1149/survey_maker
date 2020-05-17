from django.core.management.base import BaseCommand
from companies_app.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        companies = Company.objects.all()
        for item in companies:
            print(item.name)
            print(item.user_set.all())
        print('---------------')
        company = Company.objects.get(name='Тест Компания A')
        print(company)
        employees_list = company.user_set.all()
        print(len(employees_list))
        for item in employees_list:
            print(item.email)
        print('---------------')

        # few_companies = Company.objects.filter(name='Тест Компания')
        # print(few_companies)
        # print('---------------')

        # Company.objects.create(name='Test Test')
        # test_company = Company.objects.get(name='Test Test')
        # test_company.name = 'Test Test Test'
        # test_company.save()
        # print(test_company)
        # print(Company.objects.get(name='Test Test Test'))
        #
        # Company.objects.get(name='Test Test Test').delete()

        struc = company.stucture_set.all()
        print(struc)


