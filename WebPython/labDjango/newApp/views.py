from django.shortcuts import render

# Create your views here.
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def hello(request):
    return HttpResponse('hello, this is newApp')