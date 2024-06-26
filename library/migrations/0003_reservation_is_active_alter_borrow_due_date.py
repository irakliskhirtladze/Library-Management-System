# Generated by Django 5.0.4 on 2024-05-18 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_borrow_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 8, 50, 58, 955657, tzinfo=datetime.timezone.utc)),
        ),
    ]
