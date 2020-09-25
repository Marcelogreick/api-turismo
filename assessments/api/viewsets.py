from rest_framework.viewsets import ModelViewSet
from assessments.models import Assessments
from .serializers import AssessmentsSerializers


class AssessmentsViewSet(ModelViewSet):
    queryset = Assessments.objects.all()
    serializer_class = AssessmentsSerializers