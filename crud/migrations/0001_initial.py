# Generated by Django 4.1.5 on 2023-01-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('input', models.CharField(max_length=500)),
                ('output', models.CharField(max_length=500)),
                ('fromUser', models.CharField(max_length=500)),
            ],
        ),
    ]
