# Generated by Django 4.1.7 on 2023-04-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0002_remove_servicesproperty_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesproperty',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
