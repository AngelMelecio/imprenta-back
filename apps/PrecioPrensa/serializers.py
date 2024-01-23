from rest_framework import serializers
 
from apps.PrecioPrensa.models import PrecioPrensa
from apps.Tinta.serializers import TintaSerializer
from apps.Prensa.serializers import PrensaSerializer

class PrecioPrensaSerializer(serializers.ModelSerializer):
    tinta = TintaSerializer()
    prensa = PrensaSerializer()
    class Meta:
        model = PrecioPrensa
        fields = '__all__'