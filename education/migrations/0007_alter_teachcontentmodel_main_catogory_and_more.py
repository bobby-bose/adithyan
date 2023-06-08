# Generated by Django 4.1.6 on 2023-02-23 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_remove_syllabusmodel_step_6_teachcontentmodel_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachcontentmodel',
            name='main_catogory',
            field=models.CharField(blank=True, choices=[('video', 'Video'), ('mcq', 'MCQ'), ('cc', 'Clinical Case'), ('qb', 'Q-bank'), ('fc', 'Flash card')], default=None, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='teachcontentmodel',
            name='slug',
            field=models.SlugField(choices=[('video', 'Video'), ('mcq', 'MCQ'), ('cc', 'Clinical Case'), ('qb', 'Q-bank'), ('fc', 'Flash card')], default=None, null=True, unique=True),
        ),
    ]