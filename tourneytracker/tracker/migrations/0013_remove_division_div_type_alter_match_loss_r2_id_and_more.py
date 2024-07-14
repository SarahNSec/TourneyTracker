# Generated by Django 5.0.3 on 2024-07-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_location_abbreviation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='div_type',
        ),
        migrations.AlterField(
            model_name='match',
            name='loss_r2_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='R2 Loss ID'),
        ),
        migrations.AlterField(
            model_name='match',
            name='win_r2_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='R2 Win ID'),
        ),
    ]