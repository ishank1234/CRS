# Generated by Django 2.1.4 on 2019-07-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_both'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stu',
            name='id',
        ),
        migrations.AlterField(
            model_name='stu',
            name='Roll_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
