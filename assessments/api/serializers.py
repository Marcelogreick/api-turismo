from rest_framework.serializers import ModelSerializer
from assessments.models import Assessments


class AssessmentsSerializers(ModelSerializer):
    class Meta:
        model = Assessments
        fields = ['id', 'user', 'comentario', 'nota', 'data']
