# Generated by Django 2.2.2 on 2019-09-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='last_communicated_time',
            field=models.DateTimeField(null=True),
        ),
    ]
