from django.db import models

# Create your models here.

class Candidates(models.Model):
    name = models.TextField(max_length=50)
    rno = models.TextField(max_length=10, unique=True)
    blood_grp = models.TextField(max_length=5)
    
    def __str__(self):
        return self.rno
    
    