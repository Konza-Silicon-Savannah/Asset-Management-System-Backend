from django.db import models

class Asset(models.Model):
    # Django auto-generate the ID
    # id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=255)
    asset_tag = models.CharField(max_length=255, blank=True)  
    serial_number = models.CharField(max_length=255)  
    model = models.CharField(max_length=255, blank=True)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    purchase_date = models.DateField(null=True, blank=True)  
    supplier = models.CharField(max_length=255, blank=True)  
    description = models.TextField(blank=True)  
    department = models.CharField(max_length=255, null=True, blank=True)
    asset_type = models.CharField(max_length=255, null=True, blank=True)  
    location = models.CharField(max_length=255, default="Unknown")
    status = models.CharField(max_length=255, default="Active")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "asset"
        verbose_name = "asset"
        verbose_name_plural = "assets"

    def __str__(self):
        return self.name