import json

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .models import Flower
from .serializers import FlowerSerializer
             

def home(request):
    return HttpResponse("Welcome to Bloomify Flowers!")


@api_view(['GET', 'POST'])
def flower_list(request):

    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlowerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

        path('api/flowers/<int:pk>/', views.update_flower, name='update_flower'),

@api_view(['PUT'])
def update_flower(request, pk):

    try:
        flower = Flower.objects.get(pk=pk)
    except Flower.DoesNotExist:
        return Response({"error": "Flower not found"}, status=404)

    serializer = FlowerSerializer(
        flower,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)        

@api_view(['DELETE'])
def delete_flower(request, pk):

    try:
        flower = Flower.objects.get(pk=pk)
    except Flower.DoesNotExist:
        return Response(
            {"error": "Flower not found"},
            status=404
        )

    flower.delete()

    return Response(
        {"message": "Flower deleted successfully"},
        status=200
    )