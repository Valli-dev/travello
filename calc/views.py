import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html', {"name": "Valli Rocks"})
   
def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result=val1 + val2
    return render(request, 'result.html', {"result": result})
