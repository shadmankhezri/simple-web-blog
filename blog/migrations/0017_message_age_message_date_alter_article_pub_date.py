# Generated by Django 4.2.4 on 2023-09-08 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_message_created_at_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 14, 23, 56, 478799, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 8, 14, 23, 56, 476801, tzinfo=datetime.timezone.utc)),
        ),
    ]
