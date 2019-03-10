# Generated by Django 2.1.5 on 2019-02-09 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stack_overflow', '0004_auto_20190209_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='ans',
        ),
        migrations.AddField(
            model_name='answers',
            name='ans_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stack_overflow.User'),
        ),
    ]