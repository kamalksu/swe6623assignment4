# Generated by Django 4.2.6 on 2023-10-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='application_approval_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='application_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_approved_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_approved_months',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_request_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_request_months',
            field=models.IntegerField(null=True),
        ),
    ]
