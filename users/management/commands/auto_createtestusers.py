from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, help='Number of users')


    def handle(self, *args, **options):
        users = options['users']
        for id_user in range(int(users)):
            user = User(name  = f"User {id_user}")
            user.save()
            print(F"USER CREATED: id: {user.id}, Name: {user.name}")

        