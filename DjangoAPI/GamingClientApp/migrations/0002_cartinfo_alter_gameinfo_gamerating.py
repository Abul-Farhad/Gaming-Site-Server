# Generated by Django 4.2.7 on 2023-12-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingClientApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('CartId', models.AutoField(primary_key=True, serialize=False)),
                ('GameId', models.IntegerField(blank=True, null=True)),
                ('GameName', models.CharField(max_length=500)),
                ('GameImage', models.URLField(blank=True, null=True)),
                ('GameRating', models.FloatField(blank=True, null=True)),
                ('GamePrice', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='GameRating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
