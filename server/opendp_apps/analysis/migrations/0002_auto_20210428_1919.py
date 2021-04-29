# Generated by Django 3.1.2 on 2021-04-28 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataset', '0001_initial'),
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='releaseinfo',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dataset.datasetinfo'),
        ),
        migrations.AddField(
            model_name='depositorsetupinfo',
            name='dataset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='dataset.datasetinfo'),
        ),
    ]
