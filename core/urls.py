
from rest_framework import routers

from core import viewsets
from core.viewsets import ProcessamentoViewSet

router = routers.DefaultRouter()



router.register('numeros',viewsets.ProcessamentoViewSet)


urlpatterns = router.urls