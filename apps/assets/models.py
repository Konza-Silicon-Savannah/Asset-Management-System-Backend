from django.db import models

class Asset(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    Asset_Tag = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    supplier_cost = models.IntegerField(default=0)
    supplier_date = models.DateField(default="2025-01-01")
    department = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255,null=True, blank=True)
    location = models.CharField(max_length=255, default="Unknown")
    status = models.CharField(max_length=255, default="Active")


    created_at = models.DateTimeField(auto_now_add=True) #indicates when this particular asset was added to the system.


    class Meta:
        db_table = "asset"
        verbose_name = "asset"
        verbose_name_plural = "assets"

    def __str__(self):
        return self.name
    




