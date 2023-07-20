from django.shortcuts import render, redirect

# Create your views here.


def register(request):
    if request.method == "POST":
        return redirect('homepage:home')
    return render(request,'candidatereg/registration.html')
