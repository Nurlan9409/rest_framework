from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist,Album,Song
from .serializers import ArtistSerializer,AlbumSerializer,SongSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
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


"""class AlbumListAPIView(APIView):
    def get(self, request):
        albums =Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(data = serializer.data)
"""
class AlbumlAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


"""
class SongListAPIView(APIView):
    def get(self, request):
        songs =Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data = serializer.data)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        try:
            song =Song.objects.get(id=id)
            serializer = SongSerializer(song)
            return Response(data = serializer.data)
        except:
            return Response(data = {"song not found"},status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        song =Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)

        return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = Song.objects.get(id=id)
        song.delete()

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
"""

class SonglAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

