# Generated by Django 2.2.14 on 2022-06-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20220628_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='media/images/'),
        ),
    ]
