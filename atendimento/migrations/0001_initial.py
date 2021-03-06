# Generated by Django 3.1.5 on 2022-05-23 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20220523_1718'),
        ('servico', '0004_auto_20220523_1559'),
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAtendimento', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.cliente')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pet.pet')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='servico.servico')),
            ],
        ),
    ]
