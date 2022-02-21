from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    return HttpResponse("<h1>%s<h1>" % id)
