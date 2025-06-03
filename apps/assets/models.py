import uuid

from django.db import models
from uuid import uuid4

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    asset_tag = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    purchase_cost = models.IntegerField(default=0)
    supplied_date = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, default="Unknown")
    description = models.TextField(null=True, blank=True)
    status_choices = [
        ('new', 'New'),
        ('disposal', 'Disposal'),
        ('good', 'Good'),
        ('damaged', 'Damaged'),
    ]

    status = models.CharField(max_length=255, choices=status_choices, default="good")

    created_at = models.DateTimeField(
        auto_now_add=True)  # indicates when this particular asset was added to the system.

    class Meta:
        db_table = "asset"
        verbose_name = "asset"
        verbose_name_plural = "assets"

    def __str__(self):
        return self.name





