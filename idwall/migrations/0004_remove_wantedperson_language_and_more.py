# Generated by Django 4.2 on 2023-05-18 20:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("idwall", "0003_alter_wantedperson_language_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wantedperson",
            name="language",
        ),
        migrations.RemoveField(
            model_name="wantedperson",
            name="physical_description",
        ),
    ]
