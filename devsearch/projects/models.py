from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=3000, null=True, blank=True)
    source_link = models.CharField(max_length=3000, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    project_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
