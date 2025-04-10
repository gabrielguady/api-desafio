# Generated by Django 5.2 on 2025-04-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processamento',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('numero1', models.FloatField(db_column='nb_numero1')),
                ('numero2', models.FloatField(db_column='nb_numero2')),
                ('numero3', models.FloatField(db_column='nb_numero3')),
                ('status', models.CharField(default='Processando..')),
                ('media', models.FloatField(db_column='nb_media', null=True)),
                ('mediana', models.FloatField(db_column='nb_mediana', null=True)),
            ],
            options={
                'db_table': 'processamento',
                'managed': True,
            },
        ),
    ]
