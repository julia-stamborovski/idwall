# Generated by Django 4.2 on 2023-09-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("idwall", "0002_alter_wantedperson_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wantedperson",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
