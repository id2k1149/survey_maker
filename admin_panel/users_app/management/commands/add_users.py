from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from users_app.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.filter(is_superuser=False).delete()

        count = 50
        for i in range(count):
            p = (i/count)*100
            print(f'{i}) {p} %')
            mixer.blend(User)

        print('end')
