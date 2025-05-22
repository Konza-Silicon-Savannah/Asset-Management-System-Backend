from django.db import models

# Create your models here.
class Request(models.Model):
    requested_date= models.DateField(default="2025-01-01")
    requested_asset = models.CharField(max_length=255,null=True)
    requested_user=models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, default="Good Condition")


    class Meta:
        db_table = "request"
        verbose_name = "request"
        verbose_name_plural = "requests"

    def __str__(self):
        return self.requested_user
    
