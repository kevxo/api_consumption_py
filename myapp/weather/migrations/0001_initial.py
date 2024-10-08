# Generated by Django 5.1 on 2024-08-26 18:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('location', models.CharField(max_length=200)),
                ('temp_in_f', models.CharField(max_length=2)),
                ('temp_in_c', models.CharField(max_length=2)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
