# Generated by Django 2.1.8 on 2019-05-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_post_rec_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='p_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='s_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
