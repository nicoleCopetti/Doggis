# Generated by Django 3.1.5 on 2022-05-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0002_auto_20220523_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='status',
            field=models.CharField(choices=[('1', 'Aguardando Atendimento'), ('2', 'Cancelado'), ('3', 'Concluído')], default='1', max_length=10),
        ),
    ]