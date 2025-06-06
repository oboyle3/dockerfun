from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects_owned'
    )
    
    members = models.ManyToManyField(
        User, related_name='projects_joined'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name