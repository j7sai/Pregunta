# Generated by Django 2.1.5 on 2019-02-09 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack_overflow', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Answers',
        ),
    ]