# Generated by Django 3.2.12 on 2022-03-22 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lectures', '0010_auto_20220322_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 22, 23, 56, 17, 505667)),
        ),
    ]