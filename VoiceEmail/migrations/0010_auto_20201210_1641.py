# Generated by Django 3.1.1 on 2020-12-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoiceEmail', '0009_auto_20201210_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='Phone_Number',
            field=models.IntegerField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='gmail_id',
            field=models.EmailField(max_length=40, unique=True),
        ),
    ]
