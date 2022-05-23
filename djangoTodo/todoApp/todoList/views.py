from asyncio import all_tasks
from datetime import date
from email.policy import default
from pydoc import text
import re
from turtle import title
from django.shortcuts import render, redirect
from todoList.models import List
from .forms import ListForm 
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    mydict = {
        "all_tasks" : List.objects.all()
    }
    return render(request,'home.html',context=mydict)


def submit(request):
    obj = List()
    if request.method == 'GET':
            obj.taskText = request.GET.get("taskText")
            obj.taskDate = request.GET.get("taskDate")
            obj.taskDerc = request.GET.get("taskDerc")
            
            obj.save()
            mydict = {
                "all_tasks" : List.objects.all()
            }
            return redirect(home)

        
    
    else:
        mydict = {
                "all_tasks" : List.objects.all()
            }
        return render(request, 'home.html', context=mydict)


def impressum (request):
    return render(request, "impressum.html")

def newTodo (request):
    return render(request, "newTodo.html")


def edit(request,id):
    obj = List.objects.get(id=id)
    mydict = {
        "taskText" : obj.taskText,
        "taskDate" : obj.taskDate,
        "taskDerc" : obj.taskDerc,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydict)

def delete(request,id):
        obj = List.objects.get(id=id)
        obj.delete()
        mydict = {
            "all_tasks" : List.objects.all()
        }
        return redirect(home)



def edit(request,id):
    obj = List.objects.get(id=id)
    mydict = {
        "taskText" : obj.taskText,
        "taskDate" : obj.taskDate,
        "taskDerc" : obj.taskDerc,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydict)

def update(request,id):
    obj = List(id=id)
    if request.method == 'GET':
            obj.taskText = request.GET.get("taskText")
            obj.taskDate = request.GET.get("taskDate")
            obj.taskDerc = request.GET.get("taskDerc")
            obj.save()
            mydict = {
                "all_tasks" : List.objects.all()
            }
            return render(request,'home.html',context=mydict)

