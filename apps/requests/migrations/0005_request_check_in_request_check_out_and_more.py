# Generated by Django 5.2 on 2025-05-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_request_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='check_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='check_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(default='Good', max_length=255),
        ),
    ]
