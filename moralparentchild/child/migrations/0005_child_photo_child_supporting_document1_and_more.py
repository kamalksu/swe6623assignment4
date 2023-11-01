# Generated by Django 4.2.6 on 2023-11-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0004_child_login_id_alter_child_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='child',
            name='supporting_document1',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='child',
            name='supporting_document2',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
