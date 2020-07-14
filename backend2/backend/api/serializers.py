from rest_framework import serializers
#from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'location', 'phone', 'role')
        #fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user) #assign token on post
        return user
