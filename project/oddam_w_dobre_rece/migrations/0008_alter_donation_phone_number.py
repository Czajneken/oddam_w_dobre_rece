# Generated by Django 5.1 on 2024-08-18 14:07

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oddam_w_dobre_rece', '0007_donation_phone_number_donation_pick_up_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]