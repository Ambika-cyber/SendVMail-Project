# Generated by Django 3.1.1 on 2020-12-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoiceEmail', '0008_auto_20201210_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='City',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='Country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='State',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='gmail_id',
            field=models.EmailField(max_length=40),
        ),
    ]
