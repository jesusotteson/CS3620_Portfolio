# Generated by Django 2.2 on 2020-10-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0004_auto_20201011_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_message',
            field=models.CharField(max_length=500),
        ),
    ]