# Generated by Django 2.1.4 on 2019-07-19 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_Roll', models.IntegerField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
    ]