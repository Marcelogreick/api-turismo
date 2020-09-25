from rest_framework.serializers import ModelSerializer
from adresses.models import Adresses


class AdressesSerializers(ModelSerializer):
    class Meta:
        model = Adresses
        fields = ['id', 'linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude']
