from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        app_label = 'dashboard_app'
        
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    stock_status = models.CharField(max_length=20)
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name
    
class ProductionOrder(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    production_date = models.DateField()

    def __str__(self):
        return f"{self.reference} - {self.item.name}"