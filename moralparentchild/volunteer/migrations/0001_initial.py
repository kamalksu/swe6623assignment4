# Generated by Django 4.2.6 on 2023-10-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('desription', models.CharField(max_length=400)),
                ('background_cheking', models.BooleanField(default=False)),
                ('background_check_comment', models.CharField(max_length=400, null=True)),
                ('application_date', models.DateField(null=True)),
                ('application_approval_date', models.DateField(null=True)),
                ('isRemoved', models.BooleanField(default=False)),
            ],
        ),
    ]
