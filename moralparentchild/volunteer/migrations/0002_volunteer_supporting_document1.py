# Generated by Django 4.2.6 on 2023-10-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='supporting_document1',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
