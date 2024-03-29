# Generated by Django 4.2.2 on 2024-03-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.TextField()),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('Category_name', models.TextField()),
                ('Category_id', models.IntegerField()),
                ('price', models.IntegerField()),
                ('Fixed_price', models.BooleanField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
