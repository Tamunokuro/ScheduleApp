from typing import Counter
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from todo.models import Todo, Category
from .forms import TodoForm

# Create your views here.

# Fucntion to display home page


def todoForm(request, id):
    task = request.POST['task']
    date = request.POST['date']
    category = str(request.POST['category_selected'])
    Schedule_form = Todo(task=str(task), date=str(date),
                         category=Category.objects.get(name=category))
    todo = Schedule_form.save()
    return todo


def todosView(request):
    form = TodoForm()
    todoitems = Todo.objects.all().order_by("-id")
    categories = Category.objects.all()
    businessTodo = todoitems.filter(category_id=7).count()
    personalTodo = todoitems.filter(category_id=8).count()
    workTodo = todoitems.filter(category_id=9).count()
    othersTodo = todoitems.filter(category_id=10).count()


    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "todo/index.html", {
        "form": form,
        "todoitems": todoitems,
        "categories": categories,
        "businessTodo": businessTodo,
        "personalTodo": personalTodo,
        "workTodo": workTodo,
        "othersTodo": othersTodo

    })


def updateView(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TodoForm()
        else:
            todoUpdate = Todo.objects.get(pk=id)
            form = TodoForm(instance=todoUpdate)
        return render(request, "todo/todoUpdate.html", {"form": form})

    else:
        if id == 0:
            form = TodoForm(request.POST)
        else:
            todoUpdate = Todo.objects.get(pk=id)
            form = TodoForm(request.POST, instance=todoUpdate)
        if form.is_valid():
            form.save()
        return redirect("home")


def deleteView(request, id):
    toDoID = Todo.objects.get(pk=id)
    toDoID.delete()
    return redirect('home')
