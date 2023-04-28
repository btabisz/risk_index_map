from django.contrib import admin
from .models import RiskIndexItems, CountryRiskPremiumItems

# Register your models here.
admin.site.register(RiskIndexItems)
admin.site.register(CountryRiskPremiumItems)