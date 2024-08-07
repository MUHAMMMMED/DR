# Generated by Django 4.1.7 on 2023-04-02 13:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('Image', models.FileField(blank=True, null=True, upload_to='files/images/Blog/Image/%Y/%m/%d/')),
                ('Titel', models.CharField(max_length=300, null=True)),
                ('Description', models.CharField(max_length=300, null=True)),
                ('slideImage', models.FileField(blank=True, null=True, upload_to='files/images/Blog/slideImage/%Y/%m/%d/')),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
