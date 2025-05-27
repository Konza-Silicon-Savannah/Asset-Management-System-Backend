from django.db import models
from apps.assets.models import Asset
from apps.users.models import User
from uuid import uuid4

# Create your models here.
class Request(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    requested_date= models.DateTimeField(auto_now_add=True)
    requested_asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    requested_user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255, default="Good Condition")

    class Meta:
        db_table = "request"
        verbose_name = "request"
        verbose_name_plural = "requests"

    def __str__(self):
        return self.requested_user
    
