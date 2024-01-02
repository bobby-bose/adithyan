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

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError('The mobile number must be set')

        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(mobile_number, password, **extra_fields)

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=255, unique=True)
    user_scop = models.CharField(max_length=255)  # Add your desired fields here

    objects = CustomUserManager()

    # Add or modify related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        error_messages={
            'add': 'The permission could not be created.',
            'remove': 'The permission could not be removed.',
        },
    )

    def __str__(self):
        return self.username
