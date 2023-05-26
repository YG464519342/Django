# Generated by Django 4.2.1 on 2023-05-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(default=1, max_length=16, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
    ]
