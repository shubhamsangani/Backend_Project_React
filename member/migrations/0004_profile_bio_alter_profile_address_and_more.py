# Generated by Django 4.2.4 on 2023-09-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_profile_user_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobby',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
