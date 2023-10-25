# Generated by Django 4.2.6 on 2023-10-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='background_check_comment',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='application_approval_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='application_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='possible_funding',
            field=models.IntegerField(null=True),
        ),
    ]
