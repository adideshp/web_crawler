from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from django.http import HttpResponse
import json
import uuid
import pytz
from datetime import datetime
from django.utils import timezone


from .models import Job, ImageUrl, Page, Result, LeafResult, IntermediateResult
from .serializers import JobSerializer, ResultSerializer, IntermediateResultSerializer, LeafResultSerializer, PageSerializer, ImageSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer

class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Result.objects.all().order_by('-created_at')
    serializer_class = ResultSerializer

class IntermediateResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IntermediateResult.objects.all().order_by('-created_at')
    serializer_class = IntermediateResultSerializer

class LeafResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LeafResult.objects.all().order_by('-created_at')
    serializer_class = LeafResultSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all().order_by('-created_at')
    serializer_class = PageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ImageUrl.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer