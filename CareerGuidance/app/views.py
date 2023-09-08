from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def addData(request):
    return render(request, 'addData.html')