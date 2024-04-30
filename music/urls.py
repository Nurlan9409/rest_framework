from django.urls import path
from .views import LandingPageAPIView, ArtistListAPIView,AlbumListAPIView,SongListAPIView

urlpatterns =[
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artists', ArtistListAPIView.as_view(), name='artists'),
    path('albums', AlbumListAPIView.as_view(), name='albums'),
    path('songs', SongListAPIView.as_view(), name='songs'),
]