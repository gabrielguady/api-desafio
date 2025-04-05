from django.db import models

# Create your models here.

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=True,
        auto_now=True,
    )

    class Meta:
        abstract = True
        managed = True


class Processamento(ModelBase):
    numero1 = models.FloatField(
        db_column='nb_numero1',
        null=False,
    )
    numero2 = models.FloatField(
        db_column='nb_numero2',
        null=False,
    )
    numero3 = models.FloatField(
        db_column='nb_numero3',
        null=False,
    )
    status = models.CharField(
        null=False,
        default='Processando..',
        max_length=20
    )
    media = models.FloatField(
        db_column='nb_media',
        null=True,
    )
    mediana = models.FloatField(
        db_column='nb_mediana',
        null=True,
    )

    class Meta:
        db_table = 'processamento'
        managed = True
