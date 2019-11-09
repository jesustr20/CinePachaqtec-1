# Generated by Django 2.2.7 on 2019-11-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=220)),
                ('sevicio', models.TextField()),
                ('distrito', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
                'ordering': ['nombre'],
            },
        ),
    ]