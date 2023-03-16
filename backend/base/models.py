from django.db import models


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=7)
    country_id = models.CharField(max_length=3)
    risk_index = models.FloatField()

    def __str__(self):
        return f'{self.id}: ' \
               f'{self.date} - ' \
               f'{self.country_id} ' \
               f'{self.risk_index} ' 
    