# Generated by Django 3.0.5 on 2021-03-31 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210401_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.Wallet', verbose_name='Wallet`s name'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Balance'),
        ),
    ]
