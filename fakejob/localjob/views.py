from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def bhubaneswar(request):
    return render(request,'bhubaneswar.html')