# Generated by Django 4.2 on 2023-04-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopper',
            name='username',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
