from django.shortcuts import render
from rest_framework import generics, filters
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer


class WorkList(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['link']

    def get_queryset(self):
        queryset = Work.objects.all()
        work_type = self.request.query_params.get('work_type', None)
        artist_name = self.request.query_params.get('artist', None)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        if artist_name is not None:
            queryset = queryset.filter(artist__name__icontains=artist_name)
        return queryset


class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class WorkCreate(generics.CreateAPIView):
    serializer_class = WorkSerializer
