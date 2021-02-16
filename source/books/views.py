from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about_us.html')

def bestsellers(request):
    return render(request, 'bestsellers.html')

def promised_land(request):
    return render(request, 'promised_land.html')

def alchemist(request):
    return render(request, 'alchemist.html')

def little_prince(request):
    return render(request, 'little_prince.html')