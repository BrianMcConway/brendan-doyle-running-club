from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_members(request):
    return HttpResponse("Welcome to the Brendan Doyle Running Club Members Area")
