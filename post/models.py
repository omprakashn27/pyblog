from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    created_by = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return self.title
