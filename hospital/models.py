from django.db import models

class Department(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    # quantity = models.IntegerField(blank=True, null=True) #TODO - implement stock management
    
    def __str__(self) -> str:
        return self.name