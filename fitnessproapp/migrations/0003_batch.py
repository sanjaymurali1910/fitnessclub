# Generated by Django 4.0.2 on 2022-04-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessproapp', '0002_paymenttrainee_paymenttrainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('fromtime', models.TimeField(blank=True, null=True)),
                ('totime', models.TimeField(blank=True, null=True)),
                ('workout', models.CharField(max_length=100)),
                ('workoutcate', models.CharField(max_length=100)),
            ],
        ),
    ]
