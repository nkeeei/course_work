# Generated by Django 3.1.7 on 2021-04-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_auto_20210420_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studiosession',
            name='count_hours',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]