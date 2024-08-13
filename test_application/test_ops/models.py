from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TestScenario(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='test_scenario')

    def __str__(self):
        return self.title