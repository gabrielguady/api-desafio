from celery import shared_task
from core import models


@shared_task
def media(processamento_id, num1, num2, num3):
    resultado = (num1 + num2 + num3) / 3
    save_resultado.delay({
        'processamento_id': processamento_id,
        'media': resultado
    })



@shared_task
def mediana( processamento_id,num1, num2, num3):
    resultado = sorted([num1, num2, num3])[1]
    save_resultado.delay({
        'processamento_id': processamento_id,
        'mediana': resultado
    })


@shared_task
def save_resultado(params: dict):
    processamento = models.Processamento.objects.get(pk=params['processamento_id'])

    if 'media' in params:
        processamento.media = params['media']
    if 'mediana' in params:
        processamento.mediana = params['mediana']

    if processamento.media is not None and processamento.mediana is not None:
        processamento.status = "Concluído"

    processamento.save()




