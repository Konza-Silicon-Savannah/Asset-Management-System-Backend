# Generated by Django 5.2 on 2025-05-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_rename_asset_tag_asset_asset_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
