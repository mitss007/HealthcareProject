# Generated by Django 3.2.3 on 2021-05-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make_appoint',
            name='dept',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
