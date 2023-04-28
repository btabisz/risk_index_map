from rest_framework import serializers
from .models import RiskIndexItems, CountryRiskPremiumItems


class RiskIndexItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskIndexItems
        fields = '__all__'


class CountryRiskPremiumItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryRiskPremiumItems
        fields = '__all__'

