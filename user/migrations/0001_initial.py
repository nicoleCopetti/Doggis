# Generated by Django 3.1.5 on 2022-05-23 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('identidade', models.CharField(max_length=20, null=True)),
                ('isAtendente', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='pessoa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
