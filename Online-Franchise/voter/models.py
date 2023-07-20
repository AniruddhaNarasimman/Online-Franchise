from django.db import models

# Create your models here.

class VoterList(models.Model):
    firstname = models.CharField(max_length=225)
    secondname = models.CharField(max_length=225)
    rno = models.CharField(max_length = 10, null=False, unique=True, primary_key=True)

    def __str__(self):
        return self.rno
    