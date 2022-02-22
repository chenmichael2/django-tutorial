from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


def index(response, name):
    ls = ToDoList.objects.get(name=name)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s<h1><br></br><p>%s</p>" %(ls.name, str(items.text)))
