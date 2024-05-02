from django.urls import path,include
from .views import LandingPageAPIView, ArtistListAPIView,AlbumlAPIViewSet,SonglAPIViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("albums",viewset=AlbumlAPIViewSet)
router.register("songs",viewset=SonglAPIViewSet)

urlpatterns =[
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artists/', ArtistListAPIView.as_view(), name='artists'),
    path("", include(router.urls)),
    path("", include(router.urls)),

]