# Generated by Django 3.0.8 on 2020-07-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200723_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opp',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='opp',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='opp',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='past_scholars',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='past_scholars',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='past_scholars',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='tt',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tt',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='tt',
            name='updated_at',
        ),
    ]
