# Generated by Django 3.2 on 2022-09-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'обратная связь', 'verbose_name_plural': 'обратные связи'},
        ),
    ]