from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("Entire burger list: ", burgers)
    context = {
        "burgers": burgers,
    }    
    return render(request, "burger_list.html", context)

def burger_search(request):
    return render(request, "burger_search.html")

    