# Generated by Django 5.0.1 on 2024-01-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodelregistration',
            name='Confirm_Password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
