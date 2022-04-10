from django.shortcuts import render
from django.http import HttpResponse


def covidalerts(request):
    return HttpResponse(request,'covidalerts.html')