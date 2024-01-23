from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Prensa.models import Prensa
from apps.Prensa.serializers import PrensaSerializer

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def prensa_api_view(request):
    if request.method == 'POST':
        prensa_serializado = PrensaSerializer(data=request.data)
        if prensa_serializado.is_valid():
            prensa_serializado.save()
            all = PrensaSerializer( Prensa.objects.all(), many=True )
            return Response({
                'message':'¡Prensa creada correctamente!',
                'newOptsList':all.data,
                'newOptId': prensa_serializado.data.get('idPrensa')}, 
                status=status.HTTP_201_CREATED 
            )        
    if(request.method == 'GET'):
        prensas = Prensa.objects.all()
        prensas_serializado = PrensaSerializer(prensas,many=True)
        return Response( prensas_serializado.data, status=status.HTTP_200_OK )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def prensa_detail_api_view(request, pk=None ):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        prensa = Prensa.objects.filter( idPrensa = pk ).first()
        try:
            prensa.delete()
            # return the new Prensa records
            prensas = Prensa.objects.all()
            prensas_serializado = PrensaSerializer(prensas,many=True) 
            return Response({
                'message':'¡Prensa eliminada correctamente!',
                'newOptsList':prensas_serializado.data}, 
                status=status.HTTP_200_OK 
            )
        except:
            return Response({
                'message':'¡No es posible eliminar una prensa en uso!'}, 
                status=status.HTTP_409_CONFLICT 
            )