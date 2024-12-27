from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
  return render(request, 'homepage.html')

def layout2(request):
    return render(request, 'layout2.html')