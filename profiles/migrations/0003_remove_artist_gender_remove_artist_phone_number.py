# Generated by Django 4.2.6 on 2023-10-18 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_remove_artist_stage_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artist",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="phone_number",
        ),
    ]