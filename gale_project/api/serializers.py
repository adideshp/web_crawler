from rest_framework import serializers

from .models import Job, ImageUrl, Page, Result, LeafResult, IntermediateResult


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('_id', 'seed_url', 'depth', 'status', 'solution', 'created_at')
        depth=2


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('_id', 'intermediate_results')
        depth=2

class IntermediateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntermediateResult
        fields = ('_id', 'page', 'links', 'level', 'parent', 'leaf_results')
        depth=2


class LeafResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeafResult
        fields = ('_id', 'page', 'images', 'level')


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('_id', 'title', 'url')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUrl
        fields = ('_id', 'name', 'url')   