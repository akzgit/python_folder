from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My Second App</em>")


def help(request):
    return render(request, 'help.html')