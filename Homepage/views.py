from django.shortcuts import render

def index(request):
    return render(request, 'home.html', context={ "meta" : {"title" : "Goober Pool Control"} })
