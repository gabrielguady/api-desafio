from rest_framework import serializers

from core import models


class ProcessamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Processamento
        fields = '__all__'







