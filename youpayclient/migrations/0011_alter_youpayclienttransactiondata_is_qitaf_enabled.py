# Generated by Django 4.0.6 on 2023-10-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youpayclient', '0010_youpayclienttransactiondata_earned_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youpayclienttransactiondata',
            name='is_qitaf_enabled',
            field=models.BooleanField(blank=True, db_index=True, default=False, null=True),
        ),
    ]
