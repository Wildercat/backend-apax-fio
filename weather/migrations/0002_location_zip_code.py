# Generated by Django 3.2.2 on 2021-05-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=models.CharField(default=40511, max_length=5),
            preserve_default=False,
        ),
    ]
