# Generated by Django 3.1.3 on 2020-12-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentPassword',
            field=models.CharField(default='null', max_length=12),
        ),
    ]
