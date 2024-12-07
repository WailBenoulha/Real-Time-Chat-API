from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializers import getuserSerializer
from rest_framework.response import Response
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list_user_view(request):
    user_obj = User.objects.exclude(id=request.user.id)  
    serializer = getuserSerializer(user_obj, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)