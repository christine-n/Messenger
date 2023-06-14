from django.http import HttpResponse
from django.shortcuts import render
from .producer import publish

# Create your views here.
def index(request):
    publish({'name': 'John'})
    return HttpResponse("Hello, world. You're at the publisher index.")  