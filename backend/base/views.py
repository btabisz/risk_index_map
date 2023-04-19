from rest_framework.decorators import api_view
from rest_framework.response import Response
from .fetch_country_risk_premium import add_country_risk_premium_data
from .fetch_stock_market_data import stooq_add_to_db, yahoo_add_to_db
from .models import RiskIndexItems, CountryRiskPremiumItems
from .serializers import RiskIndexItemsSerializer, CountryRiskPremiumItemsSerializer
from django.http import HttpResponse
from .fetch_risk_index_data import add_risk_index_data


@api_view(['GET'])
def get_risk_index_items(request):
    data = RiskIndexItems.objects.all()
    serializer = RiskIndexItemsSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_risk_index_item(request, pk):
    data = RiskIndexItems.objects.filter(date=pk)
    serializer = RiskIndexItemsSerializer(data, many=True)
    return Response(serializer.data)


def update_rim(request):
    add_risk_index_data()
    stooq_add_to_db()
    yahoo_add_to_db()

    return HttpResponse("Updated!")


@api_view(['GET'])
def get_country_risk_premium_items(request):
    data = CountryRiskPremiumItems.objects.all()
    serializer = CountryRiskPremiumItemsSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_risk_premium_item(request, pk):
    data = CountryRiskPremiumItems.objects.filter(year=pk)
    serializer = CountryRiskPremiumItemsSerializer(data, many=True)
    return Response(serializer.data)


def update_crpm(request):
    add_country_risk_premium_data()

    return HttpResponse("Updated!")




