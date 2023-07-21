from .models import Candidates
from django.forms import ModelForm,DateInput
class CandidatesForm(ModelForm):
    class Meta:
        model = Candidates
        fields='__all__'
        widgets={
            'dob':DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','placeholder':'Select a date','type':'date'})
        }