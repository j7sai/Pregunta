# Generated by Django 2.1.5 on 2019-02-09 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stack_overflow', '0002_auto_20190209_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
