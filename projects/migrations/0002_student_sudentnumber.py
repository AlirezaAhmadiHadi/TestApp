# Generated by Django 3.2.4 on 2022-12-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sudentNumber',
            field=models.IntegerField(default=0),
        ),
    ]