# Generated by Django 4.2.4 on 2023-12-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_event_notified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('start', models.DateTimeField()),
            ],
        ),
    ]
