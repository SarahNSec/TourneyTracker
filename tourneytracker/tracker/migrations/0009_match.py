# Generated by Django 5.0.3 on 2024-03-05 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_outcome_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_start_time', models.DateTimeField()),
                ('actual_start_time', models.DateTimeField()),
                ('actual_end_time', models.DateTimeField()),
                ('r2_id', models.CharField(max_length=50, verbose_name='R2 ID')),
                ('win_r2_id', models.CharField(max_length=50)),
                ('loss_r2_id', models.CharField(max_length=50, verbose_name='R2 ID')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.court')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.division')),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.outcome')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.status')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.team')),
            ],
        ),
    ]
