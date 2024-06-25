# Generated by Django 5.0.6 on 2024-06-24 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acconts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_group', models.CharField(max_length=100)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acconts.student')),
            ],
        ),
    ]
