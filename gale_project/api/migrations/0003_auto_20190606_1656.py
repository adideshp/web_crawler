# Generated by Django 2.2.2 on 2019-06-06 16:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190606_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='intermediate_results',
        ),
        migrations.AddField(
            model_name='job',
            name='solution',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='result',
            name='result',
            field=models.ManyToManyField(blank=True, to='api.IntermediateResult'),
        ),
        migrations.AlterField(
            model_name='job',
            name='result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Result'),
        ),
    ]
