from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist
from .serializers import ArtistListSerializer
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def artists_create(request):
    if request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)