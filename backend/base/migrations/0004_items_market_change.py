# Generated by Django 4.1.7 on 2023-03-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_items_risk_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='market_change',
            field=models.FloatField(default=0),
        ),
    ]
