# Generated by Django 2.1.4 on 2019-07-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20190718_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Both',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.IntegerField()),
                ('stu_id', models.IntegerField()),
            ],
        ),
    ]