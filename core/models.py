from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model) :
    role_choices = (
        ('recruiter','Recruiter'),
        ('canditate','Canditate')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=role_choices)

    def __str__(self) :
        return f"{self.user.username} - {self.role}"
    

class Job(models.Model) :
    recruiter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null = True,blank = True)
    description = models.TextField()
    location = models.CharField(max_length=100,null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return self.title
    
