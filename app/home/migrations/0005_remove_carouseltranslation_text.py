# Generated by Django 3.2 on 2022-09-15 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_feedback_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouseltranslation',
            name='text',
        ),
    ]