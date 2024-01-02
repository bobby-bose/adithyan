from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.fields import SerializerMethodField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenObtainSerializer
from rest_framework.response import Response
from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()

# User Serializer - OK
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


#User listing with department Name and department as FK  - OK
class UserListSerializer(serializers.ModelSerializer):
    department_name = SerializerMethodField(read_only=True)

    def get_department_name(self, obj):
        if obj.department:
            return obj.department.name
        return None

    class Meta:
        model = User
        exclude = ['password']



# Login serializer
class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, validated_data):
        username = validated_data['username']
        password = validated_data.pop('password')
        return validated_data







from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=255)

    def validate(self, data):
        mobile_number = data.get("mobile_number", None)

        # You can perform additional validation logic if needed

        return data


# Change Password serializer
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You don't have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()
        response = "Password updated successfully"
        status_code = 200
        return Response(response, status=200)

 # Dont know about this Serializer   - OK
class DetailedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'email',
                  'status', 'is_active', 'is_verified',
                  ]
        # depth = 1


#**************// USED SERIALIZER//*********************#
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1
class MoodSerializer(serializers.ModelSerializer):
    mood=serializers.CharField()
    class Meta:
        model = UserProfile
        fields = ['mood']
class MoodlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['mood','id']
class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['position','email','name']        
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'        


