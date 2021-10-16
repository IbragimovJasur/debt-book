from django.db import models

class Currency(models.Model):
    class Meta:
        db_table = 'currencies'

    name = models.CharField(
        "Name", max_length=50)
    symbol = models.CharField(
        "Symbol", max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name