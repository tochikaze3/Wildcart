# Generated by Django 3.2.7 on 2022-04-14 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20220216_0250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-date_created']},
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_Description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_Name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='weight',
        ),
        migrations.AddField(
            model_name='products',
            name='Product_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stores.category'),
        ),
        migrations.AddField(
            model_name='products',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='upload_Product_Image',
            field=models.ImageField(default='default.jpg', upload_to='staticfiles/products'),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(default='', help_text='Describe your services ', max_length=250)),
                ('service_description', models.TextField(default='', max_length=1000)),
                ('payment_method', models.CharField(choices=[('pp', 'Pay per Hour'), ('p', 'Partition'), ('FR', 'Flat Rate')], default='', max_length=250)),
                ('service', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stores.vendor')),
            ],
        ),
    ]