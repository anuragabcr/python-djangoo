from django.urls import path
from .views import WatchListAV, WatchDetailAV, StreamListAV, StreamDetailAV, ReviewListAV, ReviewDetailAV, WatchReviewAV

urlpatterns = [
    path('watch/list', WatchListAV.as_view(), name='movie-list'),
    path('watch/<int:pk>', WatchDetailAV.as_view(), name='individual movie'),
    path('watch/<int:pk>/review', WatchReviewAV.as_view(), name='individual-movie-review'),
    path('stream/list', StreamListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='individual stream'),
    path('review/list', ReviewListAV.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetailAV.as_view(), name='individual review'),
]
