# Generated by Django 3.1.3 on 2020-12-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20201219_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='LGA1',
            field=models.CharField(choices=[('1', '1 - Very Confident with Critical Analysis'), ('2', '2 - Confident with Critical Analysis'), ('3', '3 - Unsure (Auto-Enrol)'), ('4', '4 - Not Confident with Critical Analysis (Auto-Enrol)'), ('5', '5 - No Prior Knowledge of Critical Analysis (Auto-Enrol)')], default='', help_text='If you score 3 or higher you will be enroled on the Critical Analysis short course for free. (Cource Reference UOBSCCA2021)', max_length=256, verbose_name='Critical Analysis'),
        ),
        migrations.AlterField(
            model_name='student',
            name='LGA2',
            field=models.CharField(choices=[('1', '1 - Very Confident with Technical Documentation'), ('2', '2 - Confident with Technical Documentation'), ('3', '3 - Unsure (Auto-Enrol)'), ('4', '4 - Not Confident with Technical Documentation (Auto-Enrol)'), ('5', '5 - No Prior use of Technical Documentation (Auto-Enrol)')], default='', help_text='If you score 3 or higher you will be enroled on the Technical Documentation short course for free. (Cource Reference UOBSCTD2021)', max_length=256, verbose_name='Technical Documentation'),
        ),
        migrations.AlterField(
            model_name='student',
            name='LGA3',
            field=models.CharField(choices=[('1', '1 - Very Confident with working in a team'), ('2', '2 - Confident with working in a team'), ('3', '3 - Unsure (Auto-Enrol)'), ('4', '4 - Not Confident with working in a team (Auto-Enrol)'), ('5', '5 - No Prior Experience of working in a team (Auto-Enrol)')], default='', help_text='If you score 3 or higher you will be enroled on the Team Work & Communication short course for free. (Cource Reference UOBSCTW2021)', max_length=256, verbose_name='Team Work & Communication'),
        ),
        migrations.AlterField(
            model_name='student',
            name='LGA4',
            field=models.CharField(choices=[('1', '1 - Very Confident with Time Management'), ('2', '2 - Confident with Time Management'), ('3', '3 - Unsure (Auto-Enrol)'), ('4', '4 - Not Confident with Time Management (Auto-Enrol)'), ('5', '5 - No Prior Knowledge of Time Management practices (Auto-Enrol)')], default='', help_text='If you score 3 or higher you will be enroled on the Time Management short course for free. (Cource Reference UOBSCTM2021)', max_length=256, verbose_name='Time Management'),
        ),
        migrations.AlterField(
            model_name='student',
            name='LGA5',
            field=models.CharField(choices=[('1', '1 - Very Confident with Word Processing and Database Applications'), ('2', '2 - Confident with Word Processing and Database Applications'), ('3', '3 - Unsure (Auto-Enrol)'), ('4', '4 - Not Confident with Word Processing and Database Applications (Auto-Enrol)'), ('5', '5 - No Prior Knowledge of Word Processing and Database Applications (Auto-Enrol)')], default='', help_text='If you score 3 or higher you will be enroled on the Computer Applications short course for free. (Cource Reference UOBSCCA2021)', max_length=256, verbose_name='Word Processing and Database Applications'),
        ),
    ]
