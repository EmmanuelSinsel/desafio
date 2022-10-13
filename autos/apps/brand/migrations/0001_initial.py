# Generated by Django 4.1.2 on 2022-10-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
    ]
