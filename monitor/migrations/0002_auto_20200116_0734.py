# Generated by Django 2.1 on 2020-01-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='monitor_cpu',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='monitor_disk',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='monitor_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='monitor_men',
            field=models.FloatField(blank=True),
        ),
    ]