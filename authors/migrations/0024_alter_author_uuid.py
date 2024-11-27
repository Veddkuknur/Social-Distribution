# Generated by Django 5.0.2 on 2024-02-27 13:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0023_alter_author_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.CharField(default=uuid.UUID('28f8caef-c899-42b2-adc6-e29589406474'), editable=False, max_length=50, unique=True),
        ),
    ]
