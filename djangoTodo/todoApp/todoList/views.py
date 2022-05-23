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

# def submit(request): 
#     obj = List()
#     obj.text = request.GET['text']
#     obj.date = request.GET['date']
#     obj.perc = request.GET['perc']
#     obj.save()
#     dic = {
#         "allTodos" : List.objects.all()
#     }
#     return render(request, 'list.html', context=dic)

# def addTodo(request):
#     todo_list = List.objects.order_by('id')
#     form = ListForm()


#     context = {'todo_list' : todo_list, 'form' : form}

#     return render(request, 'home.html', context)


def submit(request):
    obj = List()
    if request.method == 'GET':
            obj.taskText = request.GET.get("taskText")
            obj.taskDate = request.GET.get("taskDate")
            obj.taskDerc = request.GET.get("taskDerc")
            # obj.taskText = request.POST['taskText']
            # obj.taskDate = request.POST['taskDate']
            # obj.taskDerc = request.POST['taskDerc']
            obj.save()#
            mydict = {
                "all_tasks" : List.objects.all()
            }
            return redirect(home)

            #return render(request, 'home.html', context=mydict)
    
    else:
        mydict = {
                "all_tasks" : List.objects.all()
            }
        return render(request, 'home.html', context=mydict)


# def newTodo(request):
#     if request.method == 'POST':
#          taskText = request.POST.get('taskText')
#          taskDate = request.POST.get('taskDate')
#          taskDerc = request.POST.get('taskDerc')
#         #  form = ListForm(request.POST or None)

#          all_tasks = List(taskText=taskText, taskDate = taskDate, taskDerc = taskDerc)
#          all_tasks.save()
#          if all_tasks.is_valid():
#              all_tasks.save()
#             #  all_tasks=List.objects.all
             
#          return render(request, 'newTodo.html', {'all_tasks': all_tasks})

#     else:
#          all_tasks = List.objects.all
#          return render (request, 'newTodo.html', {'all_tasks': all_tasks})


def impressum (request):
    return render(request, "impressum.html")

def newTodo (request):
    return render(request, "newTodo.html")

def list(request):
    mydict = {
        "all_tasks" : List.objects.all()
    }
    return render(request,'list.html',context=mydict)

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

