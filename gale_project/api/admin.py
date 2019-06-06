from django.contrib import admin

# Register your models here.
from .models import Job, ImageUrl, Page, Result, LeafResult, IntermediateResult

admin.site.register([Job, ImageUrl, Page, Result, LeafResult, IntermediateResult])