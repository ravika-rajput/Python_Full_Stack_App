# Generated by Django 4.2.4 on 2023-09-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('rent_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('LR', 'Living Room'), ('BR', 'Bed Room'), ('SR', 'Study Room'), ('KT', 'Kitchen')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
