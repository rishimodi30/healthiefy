from django.shortcuts import redirect,render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')