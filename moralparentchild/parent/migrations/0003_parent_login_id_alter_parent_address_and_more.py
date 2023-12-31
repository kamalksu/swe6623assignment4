# Generated by Django 4.2.6 on 2023-10-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0002_parent_background_check_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='login_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='application_approval_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='application_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='background_check_comment',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='desription',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='parent',
            name='possible_funding',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='profession',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='parent',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
