# Generated by Django 3.2.12 on 2022-03-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0007_alter_room_time_occupied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='eth_s',
        ),
        migrations.AddField(
            model_name='room',
            name='ethernet_sockets',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='functioning_electrical_sockets',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
