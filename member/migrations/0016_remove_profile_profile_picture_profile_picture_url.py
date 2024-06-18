# Generated by Django 4.2.4 on 2024-04-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_alter_profile_address_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_url',
            field=models.URLField(default='', null=True),
        ),
    ]
