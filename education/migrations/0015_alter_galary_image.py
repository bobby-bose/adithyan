# Generated by Django 4.1.6 on 2023-03-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0014_galary_created_at_galary_created_by_galary_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]