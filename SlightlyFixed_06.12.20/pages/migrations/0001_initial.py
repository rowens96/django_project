# Generated by Django 3.1.3 on 2020-12-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=20)),
                ('CourseName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PathwayID', models.CharField(max_length=20)),
                ('PathwayName', models.CharField(max_length=20)),
                ('PathwayUCASvalue', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(max_length=20)),
                ('studentForname', models.CharField(max_length=20)),
                ('studentSurname', models.CharField(max_length=20)),
                ('studentContactnumber', models.CharField(max_length=20)),
                ('studentEmail', models.EmailField(max_length=20)),
                ('studentEnglishPassed', models.BooleanField(default='false')),
                ('studentMathsPassed', models.BooleanField(default='false')),
                ('studentUCASvalue', models.CharField(max_length=20)),
            ],
        ),
    ]
