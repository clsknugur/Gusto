# Generated by Django 4.0 on 2022-12-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_about_restorant_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specials',
            name='title',
        ),
    ]