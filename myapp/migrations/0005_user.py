# Generated by Django 3.2.3 on 2021-06-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_make_appoint_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(default=0, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
