# Generated by Django 4.2.4 on 2023-09-08 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_message_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 12, 29, 26, 56747, tzinfo=datetime.timezone.utc)),
        ),
    ]
