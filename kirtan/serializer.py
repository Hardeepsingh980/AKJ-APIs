from rest_framework import serializers
from .models import Kirtan, Smaagam, Artist

class KirtanSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Kirtan
        depth = 1
        fields = ('kirtan_id','smaagam','artist','url','duration')

class SmaagamSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Smaagam
        fields = "__all__"

class ArtistSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = "__all__"