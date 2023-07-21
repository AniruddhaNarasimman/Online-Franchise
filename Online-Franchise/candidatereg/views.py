from django.shortcuts import render, redirect
from .forms import CandidatesForm
# Create your views here.


def register(request):
    form=CandidatesForm()
    if request.method == "POST":
        form=CandidatesForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        return redirect('homepage:home')
    template='candidatereg/registration.html'
    data={'form':form}
    return render(request,template,data)

