# Generated by Django 3.0.7 on 2020-06-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200630_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
