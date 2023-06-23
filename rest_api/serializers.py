#from  termios importCDSUSP
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from rest_api.serializers import PetshopModelSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet
from reserva.models import Petshop, Reserva





class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api: reserva-detail'

    )
       


    class Meta: 
        model = Petshop
        fields = '__all__'


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]