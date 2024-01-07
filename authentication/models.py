from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager  # Add this line
def get_upload_directory_path(instance, filename):
    schema_name = "public"
    if instance.id:
        path = f"{schema_name}/media_uploads/crm/{instance.id}/{filename}"
    else:
        path = f"{schema_name}/media_uploads/crm/general/{filename}"
    return path

class OtpHistory(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    otp = models.CharField(max_length=255, unique=True, null=True, blank=True)
    number = models.CharField(max_length=15, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_consultant = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=True)
    is_counselor = models.BooleanField(default=True)

    def __str__(self):
        return str(self)

    @property
    def slug_name(self):
        return "otphistory"
    
    class Meta:
        app_label = 'authentication'

class UserProfile(models.Model):
    TYPES = [("ST", "Student"), ("DR", "Doctor"), ("PRO", "Professor")]
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=180, null=True, blank=True)
    position = models.CharField(max_length=180, null=True, blank=True, choices=TYPES, default="ST")
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    mood = models.CharField(max_length=255, null=True, blank=True)
    student = models.CharField(max_length=255, null=True, blank=True)
    course = models.CharField(max_length=255, null=True, blank=True)
    package = models.CharField(max_length=255, null=True, blank=True)
    user_scop = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_directory_path, null=True, blank=True)
    shortlisted_ucity = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    @property
    def slug_name(self):
        return "user"

class UserRole(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.JSONField(null=True, default=dict)
    is_staff = models.BooleanField(default=True)
    is_consultant = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=True)
    is_counselor = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    @property
    def slug_name(self):
        return "userrole"

class UserData(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    mood = models.CharField(max_length=255)

class Question(models.Model):
    day_of_month = models.DateField()
    question_text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('ALL', 'All'),
        ('OFFERS', 'Offers'),
    )

    notification_type = models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    content = models.TextField()

    # Add other fields as needed


