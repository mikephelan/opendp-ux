# Generated by Django 3.1.8 on 2021-05-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_auto_20210505_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositorsetupinfo',
            name='dataset_questions',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='depositorsetupinfo',
            name='variable_categories',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='depositorsetupinfo',
            name='variable_ranges',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
