from django.db import models

# Create your models here.
class Available(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    votes_to_adopt = models.BooleanField(null=False, default=1)
    adopted_at = models.DateTimeField(auto_created=True)