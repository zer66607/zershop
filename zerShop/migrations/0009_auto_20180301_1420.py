# Generated by Django 2.0.2 on 2018-03-01 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zerShop', '0008_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_id',
        ),
    ]
