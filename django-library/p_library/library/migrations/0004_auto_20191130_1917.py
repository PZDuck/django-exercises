# Generated by Django 2.2.7 on 2019-12-01 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20191130_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Friend'),
        ),
    ]