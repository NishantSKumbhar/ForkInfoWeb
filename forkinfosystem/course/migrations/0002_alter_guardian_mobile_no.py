# Generated by Django 4.0.6 on 2022-07-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='mobile_no',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
