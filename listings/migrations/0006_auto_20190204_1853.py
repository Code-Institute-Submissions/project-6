# Generated by Django 2.1.3 on 2019-02-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20181202_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=20),
        ),
    ]
