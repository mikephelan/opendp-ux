# Generated by Django 3.1.8 on 2021-05-05 21:54

import django.core.serializers.json
from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0004_dataversefileinfo_depositor_setup_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetinfo',
            name='data_profile',
            field=django_cryptography.fields.encrypt(models.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
        ),
    ]
