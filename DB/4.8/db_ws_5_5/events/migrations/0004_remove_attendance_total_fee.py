# Generated by Django 4.2.11 on 2024-04-10 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_attendance_total_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='total_fee',
        ),
    ]