# Generated by Django 4.2.5 on 2023-11-24 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articolo_options_alter_giornalista_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='visualizzaioni',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
