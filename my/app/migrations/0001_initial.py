# Generated by Django 4.2.1 on 2023-05-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=64, verbose_name='密码')),
                ('age', models.CharField(max_length=12, verbose_name='年龄')),
            ],
        ),
    ]