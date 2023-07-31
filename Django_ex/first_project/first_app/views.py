from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Learning Django Framework Success") #need to link with the project folder- url.py->urlpatterns
                                                    #add app name in settings.py installed_app
