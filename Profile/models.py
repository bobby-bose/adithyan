from django.db import models

class Feeds(models.Model):
    Content = models.CharField(max_length=255,default="COMING SOON")

class SecondaryEducation(models.Model):
    BOARD_CHOICES = [
        ('ICSE', 'ICSE'),
        ('CBSE', 'CBSE'),
        ('State', 'State'),
    ]
    chooseboard = models.CharField(max_length=255, choices=BOARD_CHOICES)
    startdateyear = models.DateField()
    enddateyear = models.DateField()
    entergrade = models.DecimalField(max_digits=5, decimal_places=2)


class HigherEducation(models.Model):
    BOARD_CHOICES = [
        ('ICSE', 'ICSE'),
        ('CBSE', 'CBSE'),
        ('State', 'State'),
    ]
    chooseboard = models.CharField(max_length=255, choices=BOARD_CHOICES)
    startdateyear = models.DateField()
    enddateyear = models.DateField()
    entergrade = models.DecimalField(max_digits=5, decimal_places=2)

class Work(models.Model):
    BOARD_CHOICES = [
        ('ICSE', 'ICSE'),
        ('CBSE', 'CBSE'),
        ('State', 'State'),
    ]
    chooseboard = models.CharField(max_length=255, choices=BOARD_CHOICES)
    startdateyear = models.DateField()
    enddateyear = models.DateField()
    Pursuing = models.BooleanField(default=False)

class WorkDetails(models.Model):
    Facebook = models.URLField()
    Linkedin = models.URLField()

class Education(models.Model):
    secondaryeducation = models.ForeignKey(SecondaryEducation, on_delete=models.CASCADE)
    highereducation = models.ForeignKey(HigherEducation, on_delete=models.CASCADE)

class Favourites(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    Work = models.ForeignKey(Work, on_delete=models.CASCADE)
    WorkDetails = models.ForeignKey(WorkDetails, on_delete=models.CASCADE)
    






