# Generated by Django 3.0.5 on 2020-04-22 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodfficient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='optional_ingredients',
            new_name='notes',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='substitutions',
        ),
    ]
