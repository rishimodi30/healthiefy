from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def docguide(request):
    return HttpResponse(request,'docguide.html')