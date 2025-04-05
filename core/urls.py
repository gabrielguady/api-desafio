
from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()



router.register('numeros',viewsets.ProcessamentoViewSet)


urlpatterns = router.urls