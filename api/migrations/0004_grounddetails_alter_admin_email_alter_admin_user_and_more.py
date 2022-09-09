# Generated by Django 4.0.6 on 2022-08-21 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_admin_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroundDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groundName', models.CharField(max_length=225)),
                ('groundOpeningTime', models.TimeField()),
                ('groundClosingTime', models.TimeField()),
                ('gamesToPlay', models.CharField(max_length=225)),
                ('numberOfPlayers', models.IntegerField()),
                ('defaultPrice', models.IntegerField()),
                ('turfId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.turfdetails')),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='GroundPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotOpeningTime', models.TimeField()),
                ('slotClosingTime', models.TimeField()),
                ('price', models.IntegerField()),
                ('groundId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grounddetails')),
            ],
        ),
        migrations.CreateModel(
            name='GroundImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groundImages', models.ImageField(blank=True, null=True, upload_to='groundImages')),
                ('GroundDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.grounddetails')),
            ],
        ),
        migrations.CreateModel(
            name='CoachingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachingFlag', models.BooleanField(default=False)),
                ('startingTime', models.TimeField(blank=True)),
                ('endingTime', models.TimeField(blank=True)),
                ('groundId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.grounddetails')),
            ],
        ),
    ]
