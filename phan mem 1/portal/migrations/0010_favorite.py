# Generated by Django 3.2 on 2021-05-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_vote_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAVORITE',
            fields=[
                ('IdFavo', models.AutoField(primary_key=True, serialize=False)),
                ('IdTruong', models.IntegerField()),
                ('IdUser', models.IntegerField()),
            ],
        ),
    ]