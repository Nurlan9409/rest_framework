from rest_framework import serializers
from .models import Artist,Album,Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name","image","last_updated")


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("title","image","artist","last_updated")


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title","image","album")