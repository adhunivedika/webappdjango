# Generated by Django 4.2.4 on 2023-09-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
    ]
