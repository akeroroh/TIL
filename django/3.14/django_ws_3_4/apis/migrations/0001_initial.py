# Generated by Django 4.2.11 on 2024-03-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APOinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('api_url', models.URLField()),
                ('documentation_url', models.URLField()),
                ('auth_required', models.BooleanField()),
                ('additionl_info', models.JSONField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
