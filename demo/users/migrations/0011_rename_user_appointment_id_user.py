# Generated by Django 4.2.7 on 2024-05-22 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_id_user_appointment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='user',
            new_name='id_user',
        ),
    ]
