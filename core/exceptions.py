from rest_framework.exceptions import APIException, NotFound


class RabbitMQPublishException(APIException):
    status_code = 500
    default_detail = 'Erro ao publicar tarefa no RabbitMQ.'

class NegativeNumberException(APIException):
    status_code = 400
    default_detail = 'Números negativos não são permitidos.'

class ProcessamentoNotFoundException(NotFound):
    default_detail = "Processamento não encontrado."
