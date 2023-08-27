#from  termios import CDSUSP
#from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField


from rest_framework.permissions import IsAuthenticatedOrReadOnly


from rest_api.serializers import AgendamentoModelSerializer 
from rest_framework.authentication import TokenAuthentication

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from reserva.models import  Reserva



class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
