# Generated by Django 3.2 on 2021-04-29 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]