from django.core.management.base import BaseCommand
from companies_app.models import Company, Department
from mixer.backend.django import mixer
import string
from random import randrange



class Command(BaseCommand):

    def handle(self, *args, **options):
        alphabet_string = string.ascii_uppercase
        # alphabet_list = list(alphabet_string)
        alphabet_list = ('A', 'B', 'C')

        k = randrange(5)
        Company.objects.all().delete()
        for each in alphabet_list:
            i = 1
            print("new for ", each)
            new_name = 'Тест Компания ' + each
            print(new_name)
            Company.objects.create(name=new_name)
            company_id = int(Company.objects.get(name=new_name).id)
            print(type(company_id), " company_id =", company_id)
            dep_name = each + '-' + str(i)
            Department.objects.create(department_name=dep_name, company_id=company_id)

            while i <= 3:
                j = 1
                print("new while ", "each = ", each, "i = ", i, "j = ", j)
                dep_pk = Department.objects.get(department_name=dep_name).id
                while j <= i != 1:
                    dep_name = each + '-' + str(i) + str(j)
                    Department.objects.create(department_name=dep_name, company_id=company_id, parent_id=dep_pk)

                    print("dep created ", dep_name, dep_pk)
                    j += 1
                i += 1

        print('end')
