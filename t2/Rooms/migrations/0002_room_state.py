# Generated by Django 3.2.12 on 2022-03-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]