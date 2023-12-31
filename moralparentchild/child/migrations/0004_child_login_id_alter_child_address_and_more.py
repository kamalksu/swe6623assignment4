# Generated by Django 4.2.6 on 2023-10-30 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0003_child_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='login_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='child',
            name='application_approval_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='application_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='background_check_comment',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='child',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='desription',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_approved_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_approved_months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_request_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='fund_request_months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='school_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='child',
            name='school_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='child',
            name='school_zip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='child',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='child',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
