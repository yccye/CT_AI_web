# Generated by Django 3.1.7 on 2021-05-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20210527_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='聊天室名称'),
        ),
    ]
