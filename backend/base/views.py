from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Items
from .serializers import ItemsSerializer
from django.http import HttpResponse
from .fetch_data import fetch_data



@api_view(['GET'])
def getItems(request):
    data = Items.objects.all()
    serializer = ItemsSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getItem(request, pk):
    data = Items.objects.filter(date=pk)
    serializer = ItemsSerializer(data, many=True)
    return Response(serializer.data)

def update(request):
    fetch_data()
    return HttpResponse("Updated!")




