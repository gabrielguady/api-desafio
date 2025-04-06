
from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()



router.register('numeros',viewsets.ProcessamentoViewSet, basename='processamento')


urlpatterns = router.urls