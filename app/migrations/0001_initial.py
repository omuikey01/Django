# Generated by Django 5.0.1 on 2024-01-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModelRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
