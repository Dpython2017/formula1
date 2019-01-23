#!/usr/bin/env python
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView,RetrieveAPIView, DestroyAPIView
from .serializer import ListSerializer,DetailSerializer
from .models import Fastest_laps,Driver


class ListApi(ListAPIView):

    queryset = Fastest_laps.objects.all()

    serializer_class = ListSerializer

class LapCreateApi(ListCreateAPIView):

    queryset = Fastest_laps.objects.all()

    serializer_class = ListSerializer

class DetailApi(ListAPIView):

    queryset = Driver.objects.all()
    serializer_class = DetailSerializer


class LapUpdateApi(UpdateAPIView):

    queryset = Fastest_laps.objects.all()
    serializer_class = ListSerializer

class LapRetrieve(RetrieveAPIView):
    queryset = Fastest_laps.objects.all()
    serializer_class = ListSerializer

class LapDestroy(DestroyAPIView):
    queryset = Fastest_laps.objects.all()
    serializer_class = ListSerializer