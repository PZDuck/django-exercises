# Generated by Django 2.2.7 on 2019-12-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20191207_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='media/covers/'),
        ),
    ]