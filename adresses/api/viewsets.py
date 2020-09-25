from rest_framework.viewsets import ModelViewSet
from adresses.models import Adresses
from .serializers import AdressesSerializers


class AdressesViewSet(ModelViewSet):
    queryset = Adresses.objects.all()
    serializer_class = AdressesSerializers