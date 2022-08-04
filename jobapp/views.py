from django.shortcuts import render
from . models import Jobdesc
from .serializers import Jobdescserializer
from rest_framework import viewsets
# Create your views here.


class Jobdescview(viewsets.ModelViewSet):
    queryset = Jobdesc.objects.all()
    serializer_class = Jobdescserializer

    filterset_fields = ['title']
