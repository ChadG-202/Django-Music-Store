# Generated by Django 4.1.1 on 2022-09-30 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='request',
            new_name='question',
        ),
    ]
