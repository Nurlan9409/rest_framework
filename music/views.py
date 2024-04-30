from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist,Album,Song
from .serializers import ArtistSerializer,AlbumSerializer,SongSerializer
class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data = {"get api ":"This is get api request"})

    def post(self, request):
        return Response(data = {"post api":"This is post api request "})



class ArtistListAPIView(APIView):
    def get(self, request):
        artists =Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data = serializer.data)


class AlbumListAPIView(APIView):
    def get(self, request):
        albums =Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(data = serializer.data)


class SongListAPIView(APIView):
    def get(self, request):
        songs =Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data = serializer.data)