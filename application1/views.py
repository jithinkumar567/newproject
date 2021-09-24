from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def logfn(request):
    return HttpResponse('hello this is my webpage')