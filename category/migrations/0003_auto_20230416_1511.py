# Generated by Django 3.1 on 2023-04-16 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20230415_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sluf',
            new_name='slug',
        ),
    ]
