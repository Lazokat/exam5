# Generated by Django 4.2.3 on 2023-08-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Page1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
