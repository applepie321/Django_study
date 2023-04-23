from django.shortcuts import render

def ex(request):
    return render(request, "ex.html")

def dogs(request):
    return render(request, "dogs.html")

def adopt(request):
    return render(request, "adopt.html")

def health(request):
    return render(request, "health.html")

def wellbeing(request):
    return render(request, "wellbeing.html")