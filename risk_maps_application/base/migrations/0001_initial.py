# Generated by Django 4.1.7 on 2023-03-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=7)),
                ('country_id', models.CharField(max_length=3)),
            ],
        ),
    ]
