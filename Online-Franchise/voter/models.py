from django.db import models

# Create your models here.

class VoterList(models.Model):
    rno = models.CharField(max_length = 10, null=False, unique=True, primary_key=True)
    voted=models.BooleanField(default=False)
    def __str__(self):
        return f'voter {self.rno}'
    