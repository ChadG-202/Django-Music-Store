# Generated by Django 4.1.1 on 2022-09-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_request_contact_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='hearted',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
