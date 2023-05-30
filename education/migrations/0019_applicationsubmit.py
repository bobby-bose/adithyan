# Generated by Django 4.1.6 on 2023-04-28 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0018_alter_universitymodel_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('email_id', models.EmailField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='applicationsubmit_course', to='education.coursemodel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='applicationsubmit_created', to=settings.AUTH_USER_MODEL)),
                ('univesity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.universitymodel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Application_updated', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='applicationsubmit_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
