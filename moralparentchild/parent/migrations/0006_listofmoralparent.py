# Generated by Django 4.2.6 on 2023-11-04 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0005_alter_parent_application_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListofMoralParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possible_funding', models.IntegerField(blank=True, null=True)),
                ('background_checked', models.BooleanField(default=False, null=True)),
                ('approved', models.BooleanField(default=False, null=True)),
                ('comments', models.TextField(blank=True, max_length=400, null=True)),
                ('child_id', models.TextField(blank=True, null=True)),
                ('parent_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='parent.parent', verbose_name='Parent Name')),
            ],
        ),
    ]
