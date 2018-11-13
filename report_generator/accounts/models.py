from django.db import models

# Create your models here.
class document(models.Model):
    description = models.TextField(max_length=255, blank=True)
    file = models.FileField(upload_to="media")
