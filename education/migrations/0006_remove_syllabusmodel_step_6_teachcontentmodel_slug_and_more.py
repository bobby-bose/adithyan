# Generated by Django 4.1.6 on 2023-02-23 02:54

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_merge_20230223_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabusmodel',
            name='step_6',
        ),
        migrations.AddField(
            model_name='teachcontentmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='main_catogory', unique=True),
        ),
        migrations.AlterField(
            model_name='teachcontentmodel',
            name='image_type',
            field=models.CharField(blank=True, choices=[('video', 'Video'), ('mcq', 'MCQ'), ('cc', 'Clinical Case'), ('qb', 'Q-bank'), ('fc', 'Flash card')], max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='teachcontentmodel',
            name='main_catogory',
            field=models.CharField(blank=True, choices=[('video', 'Video'), ('mcq', 'MCQ'), ('cc', 'Clinical Case'), ('qb', 'Q-bank'), ('fc', 'Flash card')], max_length=180, null=True),
        ),
    ]