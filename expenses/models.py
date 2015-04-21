from django.db import models

class Expense(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField('date spent')
    def __str__(self):
        return self.item

