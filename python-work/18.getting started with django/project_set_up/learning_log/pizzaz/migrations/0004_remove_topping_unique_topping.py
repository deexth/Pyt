# Generated by Django 3.2.3 on 2022-01-23 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaz', '0003_alter_topping_name'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='topping',
            name='unique_topping',
        ),
    ]
