# Generated by Django 4.0.3 on 2022-04-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
    ]