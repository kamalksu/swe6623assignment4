# Generated by Django 4.2.6 on 2023-11-04 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0006_alter_child_application_date_alter_child_desription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListofMoralChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_approved', models.IntegerField(blank=True, null=True)),
                ('background_checked', models.BooleanField(default=False, null=True)),
                ('approved', models.BooleanField(default=False, null=True)),
                ('comments', models.TextField(blank=True, max_length=400, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('child_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='child.child', verbose_name='Series')),
            ],
        ),
    ]
