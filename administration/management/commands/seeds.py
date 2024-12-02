from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
 
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = "admin"
        email = "admin@admin.com"
        password = "@123bRaa1"
 
        if not User.objects.filter(username = username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write("El superusuario se creo.")
        else:
            self.stdout.write("El superusuario ya existe.")
 