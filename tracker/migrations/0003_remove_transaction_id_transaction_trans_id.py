# Generated by Django 5.1.4 on 2024-12-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_transaction_budget_id_alter_budget_transtot_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='trans_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
