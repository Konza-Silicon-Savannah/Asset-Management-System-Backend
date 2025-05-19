
import uuid
from django.db import migrations
from django.contrib.auth.hashers import make_password

def seed_super_user(apps, schema_editor):
    User = apps.get_model('users', 'User')

    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create(
            id=uuid.uuid4(),
            name="Admin",
            username="admin",
            email='admin@konza.go.ke',
            department="ICT",
            employeeNo="ICT001",
            password=make_password("admin"),
            is_superuser=True
        )


def reverse_seed_super_user(apps, schema_editor):
    User = apps.get_model('users', 'User')

    User.objects.filter(is_superuser=True).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_rename_employee_number_user_employeeno'),
    ]

    operations = [
        migrations.RunPython(seed_super_user, reverse_seed_super_user),
    ]
