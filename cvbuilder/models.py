from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='education')
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

class Skill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50, blank=True)

class Project(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)