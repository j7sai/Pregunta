# Generated by Django 2.1.5 on 2019-02-09 03:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('pub_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='questionid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_overflow.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='ans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_overflow.Questions'),
        ),
    ]
