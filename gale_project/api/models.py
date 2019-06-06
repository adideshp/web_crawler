from django.db import models
import uuid

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
    result = models.ForeignKey(to='Result', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImageUrl(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =  models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=100, blank=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Page(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
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
    links = models.ManyToManyField(Page, blank=True, related_name="intermediate_links")
    level = models.IntegerField(blank=False)
    parent = models.ForeignKey(to='Page', on_delete=models.CASCADE, related_name="intermediate_parent")
    leaf_results = models.ManyToManyField(LeafResult, blank=True, related_name="leaf_results")

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Result(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    intermediate_results = models.ManyToManyField(IntermediateResult, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)



