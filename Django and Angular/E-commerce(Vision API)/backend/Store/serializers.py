from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username', 'email', 'password','is_admin']
    

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password1', 'password2', 'is_admin')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_admin=validated_data['is_admin'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        new_token = Token.objects.create(user= user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Must include both 'username' and 'password'.")

        data['user'] = user
        return data

