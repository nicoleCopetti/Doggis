# Generated by Django 3.1.5 on 2022-05-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='precoVenda',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
