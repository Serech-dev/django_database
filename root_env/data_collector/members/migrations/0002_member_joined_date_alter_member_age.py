# Generated by Django 4.2.4 on 2023-08-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
