# Generated by Django 3.0.5 on 2021-05-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.TextField()),
                ('o', models.TextField()),
                ('h', models.TextField()),
                ('l', models.TextField()),
                ('c', models.TextField()),
                ('v_name', models.TextField()),
                ('vw', models.TextField()),
                ('t', models.TextField()),
                ('n', models.TextField()),
            ],
        ),
    ]
