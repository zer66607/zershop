# Generated by Django 2.0.2 on 2018-03-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerShop', '0017_auto_20180302_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
