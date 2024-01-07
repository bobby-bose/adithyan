from rest_framework import serializers
from .models import *

from rest_framework import serializers

class SecondaryEducationSerializer(serializers.ModelSerializer):
    BOARD_CHOICES = [
        ('ICSE', 'ICSE'),
        ('CBSE', 'CBSE'),
        ('State', 'State'),
    ]
    chooseboard = serializers.ChoiceField(choices=BOARD_CHOICES)
    startdateyear = serializers.DateField()
    enddateyear = serializers.DateField()
    entergrade = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = SecondaryEducation
        fields = ['chooseboard', 'startdateyear', 'enddateyear', 'entergrade']



class HigherEducationSerializer(serializers.ModelSerializer):
    BOARD_CHOICES = [
        ('ICSE', 'ICSE'),
        ('CBSE', 'CBSE'),
        ('State', 'State'),
    ]

    chooseboard = serializers.ChoiceField(choices=BOARD_CHOICES)
    startdateyear = serializers.DateField()
    enddateyear = serializers.DateField()
    entergrade = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = HigherEducation
        fields = ['chooseboard', 'startdateyear', 'enddateyear', 'entergrade']


class WorkSerializer(serializers.ModelSerializer):
    BOARD_CHOICES = [
        ('ICSE', 'ICSE'),
        ('CBSE', 'CBSE'),
        ('State', 'State'),
    ]

    chooseboard = serializers.ChoiceField(choices=BOARD_CHOICES)
    startdateyear = serializers.DateField()
    enddateyear = serializers.DateField()
    Pursuing = serializers.BooleanField(default=False)

    class Meta:
        model = Work
        fields = ['chooseboard', 'startdateyear', 'enddateyear', 'Pursuing']


class WorkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDetails
        fields = ['Facebook', 'Linkedin']

class EducationSerializer(serializers.ModelSerializer):
    secondaryeducation = SecondaryEducationSerializer()
    highereducation = HigherEducationSerializer()

    class Meta:
        model = Education
        fields = ['secondaryeducation', 'highereducation']

class FavouritesSerializer(serializers.ModelSerializer):
    education = EducationSerializer()
    Work = WorkSerializer()
    WorkDetails = WorkDetailsSerializer()

    class Meta:
        model = Favourites
        fields = ['education', 'Work', 'WorkDetails']
