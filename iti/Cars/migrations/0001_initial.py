# Generated by Django 4.1.1 on 2022-09-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=200000)),
                ('production_year', models.IntegerField(default=2000)),
            ],
        ),
    ]
