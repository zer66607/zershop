# Generated by Django 2.0.2 on 2018-03-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerShop', '0014_auto_20180302_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('black', 'Черный'), ('gray', 'Серый'), ('yellow', 'Желтый'), ('green', 'Зеленый'), ('red', 'Красный'), ('blue', 'Синий')], default='black', max_length=30, null=True),
        ),
    ]