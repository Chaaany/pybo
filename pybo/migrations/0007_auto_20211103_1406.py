# Generated by Django 3.1.3 on 2021-11-03 05:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0006_auto_20211103_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='voder',
            new_name='voter',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='voder',
        ),
        migrations.AddField(
            model_name='answer',
            name='voter',
            field=models.ManyToManyField(related_name='voter_Answer', to=settings.AUTH_USER_MODEL),
        ),
    ]
