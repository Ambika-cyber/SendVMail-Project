# Generated by Django 3.1.1 on 2020-12-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoiceEmail', '0007_auto_20201210_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='Phone_Number',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
