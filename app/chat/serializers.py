from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

class getuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ['id','email','first_name','last_name']