# Generated by Django 4.2.6 on 2023-10-18 22:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_is_artist"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
                default="Other",
                max_length=20,
                verbose_name="Gender",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+2348037286666",
                max_length=30,
                region=None,
                unique=True,
                verbose_name="Phone Number",
            ),
        ),
    ]
