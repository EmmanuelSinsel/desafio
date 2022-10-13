# Generated by Django 4.1.2 on 2022-10-13 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='brand.brand', verbose_name='Marca'),
        ),
    ]
