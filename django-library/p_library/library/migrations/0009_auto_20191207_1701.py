# Generated by Django 2.2.7 on 2019-12-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20191207_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by',
            field=models.ManyToManyField(related_name='friend', to='library.Friend'),
        ),
    ]
