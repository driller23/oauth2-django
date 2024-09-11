from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from oauth2_provider.models import Application

class Command(BaseCommand):
    help = 'Sets up a test user and OAuth2 application'

    def handle(self, *args, **options):
        # Create a test user
        username = 'testuser'
        password = 'testpass'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, 'test@example.com', password)
            self.stdout.write(self.style.SUCCESS(f'Created superuser: {username}'))
        
        # Create OAuth2 application
        app_name = 'Test OAuth2 App'
        client_id = 'your-client-id'
        client_secret = 'your-client-secret'
        if not Application.objects.filter(name=app_name).exists():
            Application.objects.create(
                name=app_name,
                client_id=client_id,
                client_secret=client_secret,
                user=User.objects.get(username=username),
                client_type=Application.CLIENT_CONFIDENTIAL,
                authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
                redirect_uris='http://localhost:8001/oauth/callback/'
            )
            self.stdout.write(self.style.SUCCESS(f'Created OAuth2 application: {app_name}'))
