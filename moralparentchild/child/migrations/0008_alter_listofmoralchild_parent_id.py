# Generated by Django 4.2.6 on 2023-11-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0005_alter_parent_application_date'),
        ('child', '0007_listofmoralchild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofmoralchild',
            name='parent_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='parent.parent', verbose_name='Series'),
        ),
    ]