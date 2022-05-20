# Generated by Django 3.2.7 on 2022-05-20 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='store_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stores.vendor'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
