# Generated by Django 4.1 on 2022-08-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_model',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie_model',
            name='rating',
            field=models.FloatField(verbose_name='rating'),
        ),
    ]
