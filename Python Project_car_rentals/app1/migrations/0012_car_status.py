# Generated by Django 2.2.4 on 2021-06-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20210605_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
