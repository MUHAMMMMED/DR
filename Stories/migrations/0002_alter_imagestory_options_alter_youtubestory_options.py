# Generated by Django 4.1.7 on 2023-04-02 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagestory',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='youtubestory',
            options={'ordering': ('-created_at',)},
        ),
    ]
