from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request, number):
    print(request)
    return HttpResponse(f"Hello, World!{number}")

def factorial(request):
    return HttpResponse("Tu bedzie silnia")