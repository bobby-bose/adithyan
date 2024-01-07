from rest_framework import serializers
from .models import About, Feed, Courses, Gallery

class AboutSerializer(serializers.ModelSerializer):
    UniversityName = serializers.CharField(max_length=255)
    UniversityPlace = serializers.CharField(max_length=255)
    About = serializers.CharField(max_length=255)
    ranking = serializers.IntegerField()
    UndergraduatePrograms = serializers.IntegerField()
    EXAM_CHOICES = [
        ('AFFILIATED', 'Affiliated'),
        ('NON_AFFILIATED', 'Non-Affiliated'),
    ]
    FMGE = serializers.ChoiceField(choices=EXAM_CHOICES)
    USML = serializers.ChoiceField(choices=EXAM_CHOICES)
    PLAB = serializers.ChoiceField(choices=EXAM_CHOICES)

    class Meta:
        model = About
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=255)
    TIME_CHOICES = [
    (1, '1 day ago'),
    (2, '2 days ago'),
    (3, '3 days ago'),
    (4, '4 days ago'),
    (5, '5 days ago'),
    (6, '6 days ago'),
    (7, '1 week ago'),
    (8, '8 days ago'),
    (9, '9 days ago'),
    (10, '10 days ago'),
    (11, '11 days ago'),
    (12, '12 days ago'),
    (13, '13 days ago'),
    (14, '2 weeks ago'),
    (15, '15 days ago'),
]
    Time = serializers.ChoiceField(choices=TIME_CHOICES)
    Title = serializers.CharField(max_length=255)
    Description = serializers.CharField(max_length=255)

    class Meta:
        model = Feed
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=255)
    University = serializers.CharField(max_length=255)
    Place = serializers.CharField(max_length=255)
    DURATION_CHOICES = [
        (15, '15 months'),
        (30, '30 months'),
        (45, '45 months'),
        (60, '60 months'),
    ]
    Duration = serializers.ChoiceField(choices=DURATION_CHOICES)
    SEASON_CHOICES = [
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
        ('Polar Day', 'Polar Day'),
        ('Polar Night', 'Polar Night'),
    ]
    Season = serializers.ChoiceField(choices=SEASON_CHOICES)

    class Meta:
        model = Courses
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    UniversityEntrance = serializers.URLField()
    LectureRooms = serializers.URLField()
    Laboratory = serializers.URLField()

    class Meta:
        model = Gallery
        fields = '__all__'
