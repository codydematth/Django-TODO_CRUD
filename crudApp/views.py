from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def todoView(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"todos": todos, "form": form}
    return render(request, "task.html", context)


def updateTodoView(request, id):
    todo = Todo.objects.get(id=id)
    updateForm = TodoForm(instance=todo)
    if request.method == "POST":

        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            # update existing todo in the database
            updateForm.save()
            # redirect the back to homePage
            return redirect("/")
        else:
            updateForm = TodoForm(instance=todo)

    context = {"todo": todo, "updateForm": updateForm}

    return render(request, "update_task.html", context)


def deleteTodoView(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect("/")


def is_completedView(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_complete = True
    todo.save()
    if todo.is_complete == False:
        todo.save()
    return redirect("/")
