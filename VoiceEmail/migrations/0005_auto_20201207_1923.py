# Generated by Django 3.1.1 on 2020-12-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoiceEmail', '0004_auto_20201206_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_detail',
            name='gpass',
        ),
        migrations.AddField(
            model_name='user_detail',
            name='Name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
