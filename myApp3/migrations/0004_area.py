# Generated by Django 5.1 on 2024-08-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp3', '0003_delete_vol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
    ]