# Generated by Django 4.1.6 on 2023-02-17 16:32

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=180, null=True)),
                ('position', models.CharField(blank=True, choices=[('ST', 'Student'), ('DR', 'Doctor'), ('PRO', 'professor')], default='ST', max_length=180, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('university', models.CharField(blank=True, max_length=255, null=True)),
                ('mood', models.CharField(blank=True, max_length=255, null=True)),
                ('student', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.CharField(blank=True, max_length=255, null=True)),
                ('package', models.CharField(blank=True, max_length=255, null=True)),
                ('user_scop', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=authentication.models.get_upload_directory_path)),
                ('shortlisted_ucity', models.CharField(blank=True, max_length=255, null=True)),
                ('otp_history', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='otp_updated', to='authentication.otphistory')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]