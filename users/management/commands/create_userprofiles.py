from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile


class Command(BaseCommand):
    help = 'Create UserProfile objects for existing users'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('UserProfiles created successfully.'))  # noqa
