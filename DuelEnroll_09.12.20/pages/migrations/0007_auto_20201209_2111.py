# Generated by Django 3.1.3 on 2020-12-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201209_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='PathwayName',
            field=models.CharField(choices=[('SO', 'Software Engineering'), ('NE', 'Networking')], max_length=2),
        ),
    ]