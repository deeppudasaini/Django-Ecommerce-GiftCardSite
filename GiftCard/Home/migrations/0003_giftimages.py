# Generated by Django 2.2.13 on 2021-07-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20210708_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=254)),
            ],
        ),
    ]
