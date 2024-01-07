from django.db import models

class About(models.Model):
    UniversityName = models.CharField(max_length=255)
    UniversityPlace = models.CharField(max_length=255)
    About = models.TextField()
    ranking = models.IntegerField()
    UndergraduatePrograms = models.IntegerField()
    FMGE = models.CharField(max_length=255)
    USML = models.CharField(max_length=255)
    PLAB = models.CharField(max_length=255)

class Feed(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Time = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Description = models.TextField()

class Courses(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    University = models.CharField(max_length=255)
    Place = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
    Season = models.CharField(max_length=255)

class Gallery(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    UniversityEntrance = models.URLField()
    LectureRooms = models.URLField()
    Laboratory = models.URLField()
