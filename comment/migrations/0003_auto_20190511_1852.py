# Generated by Django 2.2.1 on 2019-05-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190511_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='author',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='lost',
            name='author',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]