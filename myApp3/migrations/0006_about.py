# Generated by Django 5.1 on 2024-08-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp3', '0005_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
