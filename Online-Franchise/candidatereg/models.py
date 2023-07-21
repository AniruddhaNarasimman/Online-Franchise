from django.db import models

from voter.models import VoterList
dpt= [
    ("it", "information technology"),
    ("cse", "computer scienccce"),]
gender=[('m','male'),('f','female')]
# Create your models here.

class Candidates(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    second_name=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=50,choices=gender,null=True)
    department=models.CharField(max_length=50,choices=dpt,null=True)
    roll_no=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    photo=models.ImageField(default='default.jpg',upload_to='candidate_pics/')
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.roll_no
    
    
