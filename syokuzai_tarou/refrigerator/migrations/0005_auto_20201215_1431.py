# Generated by Django 3.1.3 on 2020-12-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refrigerator', '0004_auto_20201212_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='foodName',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]