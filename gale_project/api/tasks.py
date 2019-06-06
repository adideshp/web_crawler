from __future__ import absolute_import
import os
import logging
import requests
from celery.decorators import task
from worker.worker import app
from django.conf import settings
from crawler.crawler import Crawler

from api.models import Result, Job
logger = logging.getLogger(__name__)

"""
@app.task(bind=True, name='start_crawler_task')
def start_crawler_task(self, job_id):
    job = Job.objects.get(pk=job_id)
    
    crawler = Crawler(instance.start_url)
    result = crawler.start(instance.depth)
    print("Aditya")
    print(job._id)
    

"""