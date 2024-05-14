from django.shortcuts import render
from music.models import Artist, Album, Song
from music.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ArtisAPIViewSet(viewsets.ModelViewSet):
    queryset =Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=True, methods=['GET'])
    def listened(self, request,*args,**kwargs):
        artist= self.get_object()
        artist.listened+=1
        artist.save()
        return Response(artist.listened, status=status.HTTP_200_OK)
class AlbumAPIViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action (detail=True, methods=['GET'])
    def watched(self, request, *args, **kwargs):
        album = self.get_object()
        album.watched+=1
        album.save()
        return Response(album.watched, status=status.HTTP_200_OK)




class SongAPIViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    @action (detail=True, methods=['GET'])
    def downloaded(self, request, *args, **kwargs):
        song = self.get_object()
        song.downloaded +=1
        song.save()
        return Response(song.downloaded, status=status.HTTP_200_OK)


