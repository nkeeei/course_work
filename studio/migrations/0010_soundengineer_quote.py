# Generated by Django 3.1.7 on 2021-04-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0009_studio_opening_days_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundengineer',
            name='quote',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
