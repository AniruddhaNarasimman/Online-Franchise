from django.contrib import admin

from .models import Candidates
# Register your models here.

class AdminCandidates(admin.ModelAdmin):
    model=Candidates
    list_display=('first_name','second_name','dob','gender','department','roll_no','email','photo','votes')
admin.site.register(Candidates,AdminCandidates)