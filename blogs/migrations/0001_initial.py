# Generated by Django 2.2.14 on 2022-06-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Detail', models.CharField(max_length=200)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
    ]