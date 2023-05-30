# Generated by Django 4.1.6 on 2023-03-29 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import education.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0012_alter_bookmarks_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='galary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(blank=True, choices=[('UN', 'univesity'), ('Nl', 'null')], default='BG', max_length=180, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=education.models.get_upload_directory_path)),
                ('model_object', models.CharField(max_length=255)),
                ('image_uuid', models.UUIDField(default=uuid.uuid4, null=True, unique=True)),
                ('image_type', models.CharField(max_length=255)),
                ('univesity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.universitymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='galary_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
