# Generated by Django 4.1.2 on 2022-10-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_management_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
