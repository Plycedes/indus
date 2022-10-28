from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Abhay Pratap Yadav')

def new(request):
    return HttpResponse('New Products available')
