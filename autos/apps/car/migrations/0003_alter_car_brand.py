# Generated by Django 4.1.2 on 2022-10-13 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_alter_carmodel_options_alter_carmodel_brand'),
        ('car', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.carmodel'),
        ),
    ]
