from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model,authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields=['email','password','first_name','last_name']
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)  

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()      
    id = serializers.CharField(max_length=15,read_only=True)
    password = serializers.CharField(max_length=255,write_only=True)

    def validate(self,data):
        email = data.get('email',None)
        password = data.get('password',None)

        if email is None:
            raise serializers.ValidationError('email is required for login')
        if password is None:
            raise serializers.ValidationError('password is required for login')
        
        user = authenticate(username=email,password=password)

        if user is None:
            raise serializers.ValidationError('invalid email or password')
        if not user.is_active:
            raise serializers.ValidationError('user is not active')
        
        return user