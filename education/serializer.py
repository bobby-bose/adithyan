from asyncore import read
from rest_framework import serializers
from .models import*


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = "__all__"
    
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedModel
        fields = "__all__"
class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotModel
        fields = "__all__"

class MCQInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQInitialModel
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = "__all__"

class TeachContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachContentModel
        fields = "__all__"

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"

class bookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMarks
        fields = '__all__'
class GalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = galary
        fields = '__all__'
class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsModel
        fields = '__all__'
class applicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = '__all__'
         
class applicationSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSubmit
        fields = '__all__'
         