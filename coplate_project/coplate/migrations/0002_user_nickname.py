# Generated by Django 2.2 on 2021-07-30 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
