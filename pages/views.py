from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def breed(request):
    return render(request, 'breed.html')

def temperament(request):
    return render(request, 'temperament.html')

def care(request):
    return render(request, 'care.html')

