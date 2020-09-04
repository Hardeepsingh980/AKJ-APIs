from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Kirtan, Smaagam, Artist
from .serializer import KirtanSerialiser, ArtistSerialiser, SmaagamSerialiser

from rest_framework.views import APIView
from rest_framework import filters

from rest_framework import generics

from django.http import HttpResponse

from rest_framework.response import Response


import requests
from bs4 import BeautifulSoup as bs


class KirtanViewSet(generics.ListCreateAPIView):
    search_fields = ['smaagam__smaagam_name', 'artist__artist_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Kirtan.objects.all()
    serializer_class = KirtanSerialiser


class SmaagamList(generics.ListCreateAPIView):
    search_fields = ['smaagam__smaagam_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Kirtan.objects.all()
    serializer_class = KirtanSerialiser


class KirtanList(generics.ListCreateAPIView):
    search_fields = ['artist__artist_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Kirtan.objects.all()
    serializer_class = KirtanSerialiser


class Latest(generics.ListCreateAPIView):
    queryset = Kirtan.objects.all().order_by('-kirtan_id')
    serializer_class = KirtanSerialiser


class AllSmaagam(generics.ListCreateAPIView):
    search_fields = ['smaagam_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Smaagam.objects.all()
    serializer_class = SmaagamSerialiser


class AllArtist(generics.ListCreateAPIView):
    search_fields = ['artist_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerialiser

class GetKirtanFromSmaagam(APIView):

    def get(self, request, smaagam_id, *args, **kwargs):
        queryset = Kirtan.objects.filter(smaagam_id=smaagam_id)
        s = KirtanSerialiser(queryset, many=True)
        return Response(s.data)

class GetKirtanFromArtist(APIView):

    def get(self, request, artist_id, *args, **kwargs):
        queryset = Kirtan.objects.filter(artist_id=artist_id)
        s = KirtanSerialiser(queryset, many=True)
        return Response(s.data)


def loadAll(request, num):

    res = requests.get(f'https://www.akj.org/keertan.php?sr=1&page={num}')
    soup = bs(res.text, 'html.parser')

    samagams = soup.select('div.krtn_det')[::-1]
    samagams_lists = soup.select('div.krtn_listing')[::-1]

    for i in range(len(samagams)):
        samagam_name = samagams[i].select_one('a').getText()
        shabads = samagams_lists[i].select('tbody tr')
        l = []
        for shabad in shabads:
            try:
                title = shabad.select('td')[1].select_one(
                    'a').getText().replace('NEW', '')
                dur = shabad.select('td')[0].getText()
                try:
                    url = shabad.select('td')[3].select_one(
                        'a').attrs['href']
                except:
                    url = None
                type_ = shabad.select('td')[2].getText()
                smaagam = Smaagam.objects.filter(smaagam_name=samagam_name)
                if len(smaagam) == 0:
                    smaagam = Smaagam()
                    smaagam.smaagam_name = samagam_name
                    smaagam.save()
                else:
                    smaagam = smaagam[0]

                artist = Artist.objects.filter(artist_name=title)
                if len(artist) == 0:
                    artist = Artist()
                    artist.artist_name = title
                    artist.save()
                else:
                    artist = artist[0]

                kirtan = Kirtan()
                kirtan.artist = artist
                kirtan.smaagam = smaagam
                kirtan.url = url
                kirtan.duration = dur
                kirtan.save()
            except:
                pass

    return HttpResponse(request, 'Success')





def load(request):
    existingSmaagam = []

    s = Smaagam.objects.all().order_by('-smaagam_id')[:100]

    for i in s:
        existingSmaagam.append(i.smaagam_name)

    res = requests.get('https://www.akj.org/keertan.php')

    soup = bs(res.text, 'html.parser')

    samagams = soup.select('div.krtn_det')[::-1]
    samagams_lists = soup.select('div.krtn_listing')[::-1]

    for i in range(len(samagams)):
        samagam_name = samagams[i].select_one('a').getText()
        if samagam_name not in existingSmaagam:
            print(samagam_name)
            shabads = samagams_lists[i].select('tbody tr')
            l = []
            for shabad in shabads:
                try:
                    title = shabad.select('td')[1].select_one(
                        'a').getText().replace('NEW', '')
                    dur = shabad.select('td')[0].getText()
                    try:
                        url = shabad.select('td')[3].select_one(
                            'a').attrs['href']
                    except:
                        url = None
                    type_ = shabad.select('td')[2].getText()
                    smaagam = Smaagam.objects.filter(smaagam_name=samagam_name)
                    if len(smaagam) == 0:
                        smaagam = Smaagam()
                        smaagam.smaagam_name = samagam_name
                        smaagam.save()
                    else:
                        smaagam = smaagam[0]

                    artist = Artist.objects.filter(artist_name=title)
                    if len(artist) == 0:
                        artist = Artist()
                        artist.artist_name = title
                        artist.save()
                    else:
                        artist = artist[0]

                    kirtan = Kirtan()
                    kirtan.artist = artist
                    kirtan.smaagam = smaagam
                    kirtan.url = url
                    kirtan.duration = dur
                    kirtan.save()
                except:
                    pass

    return HttpResponse(request, 'Success')
