# Generated by Django 3.1.6 on 2021-04-15 20:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0002_auto_20210412_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ManyToManyField(default=None, null=True, related_name='Creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
