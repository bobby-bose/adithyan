# Generated by Django 4.1.6 on 2023-03-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0016_alter_galary_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='syllabusmodel',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='teachcontentmodel',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
