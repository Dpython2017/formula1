#!/usr/bin/env python
from rest_framework.generics import ListAPIView
from .serializer import ListSerializer
from .models import Fastest_laps


class ListApi(ListAPIView):

    queryset = Fastest_laps.objects.all()

    serializer_class = ListSerializer

