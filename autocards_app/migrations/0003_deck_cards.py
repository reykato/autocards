# Generated by Django 4.2.6 on 2023-10-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocards_app', '0002_deck_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(to='autocards_app.card'),
        ),
    ]
