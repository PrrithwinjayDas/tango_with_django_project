from django.shortcuts import render

def index(request):
    context = {
        "name": "Rango",
        "visits": 5,
    }
    return render(request, "rango/index.html", context)
