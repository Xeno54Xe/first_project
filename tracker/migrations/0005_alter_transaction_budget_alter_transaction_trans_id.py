# Generated by Django 5.1.4 on 2024-12-28 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_transaction_budget_id_transaction_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='tracker.budget'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trans_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
