from django.urls import path
from .views import WorkList, ArtistList, WorkCreate


urlpatterns = [
    path('api/works', WorkList.as_view(), name='work_list'),
    path('api/artists', ArtistList.as_view(), name='artist_list'),
    path('api/works/create', WorkCreate.as_view(), name='work_create'),
]
