# Generated by Django 5.0.6 on 2024-05-24 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_ad_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ad_login',
            new_name='login',
        ),
    ]
