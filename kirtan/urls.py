from django.urls import path
from . import views

urlpatterns = [
    path('load/', views.load),
    # path('loadall/<int:num>', views.loadAll),
    path('latest/', views.Latest.as_view()),
    path('smaagam/', views.SmaagamList.as_view()),
    path('artist/', views.KirtanList.as_view()),
    path('allsmaagam/', views.AllSmaagam.as_view()),
    path('allartist/', views.AllArtist.as_view()),
    path('getbysmaagam/<int:smaagam_id>', views.GetKirtanFromSmaagam.as_view()),
    path('getbyartist/<int:artist_id>', views.GetKirtanFromArtist.as_view()),
]