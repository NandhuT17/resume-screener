from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model) :
    job_title = models.CharField()
    job_description = models.TextField()
    required_skills = models.CharField()
    required_experience = models.IntegerField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.TimeField(auto_now_add = True)

    def __str__(self) :
        return self.job_title