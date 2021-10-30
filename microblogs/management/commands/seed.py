from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range (0,100):
            name = self.faker.name()
            first_name = name.split(' ')[0]
            last_name = ' '.join(name.split(' ')[-1:])
            username = '@' + first_name.lower() + last_name.lower().replace(' ','')
            email = first_name.lower() + '.' + last_name.lower() + '@example.org'
            bio = self.faker.text()

            user = User.objects.create_user(username)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.bio = bio

            user.save()
