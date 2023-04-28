from django.db import models


class RiskIndexItems(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=7)
    country_id = models.CharField(max_length=3)
    risk_index = models.FloatField()
    risk_change = models.FloatField(default=0.0001)
    risk_delta = models.FloatField(default=0.0001)
    market_index_name = models.CharField(max_length=20, default="No data")
    market_change = models.FloatField(default=0.0001)

    def __str__(self):
        return f'{self.id}: ' \
               f'{self.country_id}, ' \
               f'{self.date}'


class CountryRiskPremiumItems(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    country_id = models.CharField(max_length=3)
    country_risk_premium = models.FloatField(default=0.0001)

    def __str__(self):
        return f'{self.id}: ' \
               f'{self.country_id}, ' \
               f'{self.year}'

