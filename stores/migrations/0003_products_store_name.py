# Generated by Django 3.2.7 on 2022-02-23 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='store_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stores.vendor'),
        ),
    ]
