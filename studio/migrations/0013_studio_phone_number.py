# Generated by Django 3.1.7 on 2021-05-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_auto_20210430_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
