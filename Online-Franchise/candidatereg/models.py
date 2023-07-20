from django.db import models

from voter.models import VoterList

# Create your models here.

class Candidates(models.Model):
    name = models.CharField(max_length=50)
    rno = models.ForeignKey(VoterList, on_delete=models.CASCADE)
    blood_grp = models.CharField(max_length=5)
    
    def __str__(self):
        return self.rno
    
    
