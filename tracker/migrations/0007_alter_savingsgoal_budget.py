# Generated by Django 5.1.4 on 2024-12-28 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_alter_transaction_budget_alter_transaction_trans_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingsgoal',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='savings_goals', to='tracker.budget'),
        ),
    ]
