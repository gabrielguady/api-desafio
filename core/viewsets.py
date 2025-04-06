from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from core import models, serializers, tasks
from core.exceptions import RabbitMQPublishException, ProcessamentoNotFoundException


class ProcessamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Processamento.objects.all()
    serializer_class = serializers.ProcessamentoSerializer

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        try:
            processamento = self.get_object()
            data = {
                "id": processamento.id,
                "status": processamento.status,
                "media": processamento.media,
                "mediana": processamento.mediana,
            }
            return Response(data, status=HTTP_200_OK)
        except models.Processamento.DoesNotExist:
            raise ProcessamentoNotFoundException()

    @action(detail=False, methods=['post'])
    def processar(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        id_processamento = obj.id

        try:
            tasks.media.delay(
                id_processamento,
                serializer.validated_data["numero1"],
                serializer.validated_data["numero2"],
                serializer.validated_data["numero3"]
            )
            tasks.mediana.delay(
                id_processamento,
                serializer.validated_data["numero1"],
                serializer.validated_data["numero2"],
                serializer.validated_data["numero3"]
            )
            return Response({"id": id_processamento, "status": "Processando"}, status=status.HTTP_201_CREATED)
        except Exception:
            raise RabbitMQPublishException()
