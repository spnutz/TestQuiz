# Generated by Django 2.0.1 on 2018-06-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20180615_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='question',
            name='choice1',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='choice2',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
