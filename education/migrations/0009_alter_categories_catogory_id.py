# Generated by Django 4.1.6 on 2023-03-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_categories_remove_teachcontentmodel_image_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='catogory_id',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
