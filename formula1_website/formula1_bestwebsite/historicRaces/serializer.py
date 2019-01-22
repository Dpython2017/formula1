#!/usr/bin/env python
from rest_framework import serializers
from .models import Fastest_laps

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fastest_laps
        fields = '__all__'

