# Generated by Django 2.2.7 on 2019-11-10 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='psinosis',
            new_name='sinopsis',
        ),
    ]
