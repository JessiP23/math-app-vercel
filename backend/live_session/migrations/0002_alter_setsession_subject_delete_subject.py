# Generated by Django 5.0.1 on 2024-01-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_session', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setsession',
            name='subject',
            field=models.CharField(max_length=60),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
