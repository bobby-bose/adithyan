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
from .models import UserData, Question, Notification
from rest_framework import serializers

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
    country_code=serializers.CharField(max_length=255)
    mobile_number = serializers.CharField(max_length=255)

    def validate(self, data):
        mobile_number = data.get("mobile_number", None)
        country_code = data.get("country_code", None)

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


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'



class QuestionSerializer(serializers.Serializer):
    day_of_month = serializers.DateField()
    question_text = serializers.CharField(max_length=255)
    option_1 = serializers.CharField(max_length=255)
    option_2 = serializers.CharField(max_length=255)
    option_3 = serializers.CharField(max_length=255)
    option_4 = serializers.CharField(max_length=255)

    def validate(self, data):


        return data

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.day_of_month = validated_data.get('day_of_month', instance.day_of_month)
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.option_1 = validated_data.get('option_1', instance.option_1)
        instance.option_2 = validated_data.get('option_2', instance.option_2)
        instance.option_3 = validated_data.get('option_3', instance.option_3)
        instance.option_4 = validated_data.get('option_4', instance.option_4)
        instance.save()
        return instance

class NotificationSerializer(serializers.Serializer):
    NOTIFICATION_TYPES = (
        ('ALL', 'All'),
        ('OFFERS', 'Offers'),
    )

    notification_type = serializers.ChoiceField(choices=NOTIFICATION_TYPES)
    content = serializers.CharField()

    def validate(self, data):
        # You can perform additional validation logic if needed

        return data

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.notification_type = validated_data.get('notification_type', instance.notification_type)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

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


