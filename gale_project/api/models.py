from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from crawler.crawler import Crawler
from django.contrib.postgres.fields import JSONField


JOB_STATUS = (
    ("COMPLETED", "Completed"),
    ("FAILED", "Failed"),
    ("PROCESSING", "Processing"),
)

class Job(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seed_url = models.CharField(max_length=100, blank=False)
    depth = models.IntegerField(blank=False, default=1)
    status = models.CharField(choices=JOB_STATUS, max_length=20, blank=False, default="PROCESSING")
    solution = JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Job)
def start_crawler_post_save(sender, instance, created, **kwargs):
    crawler = Crawler(instance.seed_url)
    instance.result = crawler.start(instance.depth)
    instance.status = "COMPLETED"
    instance.save()


class ImageUrl(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =  models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=100, blank=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Page(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class LeafResult(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey(to='Page', on_delete=models.CASCADE)
    images = models.ManyToManyField(ImageUrl, blank=True, related_name="leaf_images")
    level = models.IntegerField(blank=False)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class IntermediateResult(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey(to='Page', on_delete=models.CASCADE, related_name="intermediate_page")
    level = models.IntegerField(blank=False)
    parent = models.ForeignKey(to='Page', on_delete=models.CASCADE, related_name="intermediate_parent")
    leaf_results = models.ManyToManyField(LeafResult, blank=True, related_name="leaf_results")
    intermediate_results = models.ManyToManyField(to='self', blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Result(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    result = models.ManyToManyField(IntermediateResult, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)



