from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Todo
from django.contrib import messages
from .forms import EditTodoItem
from .models import *
from .forms import *
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    items = Todo.objects.all().order_by('added_date')
    data={
            'items':items,
    }
    return render(request, 'index.html', data)
# @csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        added_date = timezone.now()
        item = request.POST['content']
        if item != '':
            messages.success(request,'Congratulation!! Item are Added')
            Todo(added_date=added_date, item=item).save()
            return redirect(home)
        else:
            messages.success(request,'Please fill the item data in input field')
            return redirect(home)
    return render(request, 'index.html')
# @csrf_exempt
def edit_item(request, pk):
    todo = Todo.objects.get(id=pk)
    print(f'todo item is {todo}')
    form = EditTodoItem(instance=todo)
    if request.method == 'POST':
        form = EditTodoItem(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully!! Item are Edited')
            return redirect(home)
    data = {
        'form':form
    }
    return render(request, 'edit.html', data)
     

def delete_item(request, id):
    item_id = id
    messages.success(request,'Successfully!! Item are deleted')
    Todo.objects.filter(id=item_id).delete()
    return redirect(home)

    
def crossoff(request, pk):
    item = Todo.objects.get(id = pk)
    item.completed = False
    item.save()
    messages.success(request,'Item are Uncrossed')

    return redirect(home)

def uncross(request,pk):
    if request.method == 'GET':
        item = Todo.objects.get(id = pk)
        item.completed = True
        item.save()
        messages.success(request,'Item are Crossed')

        return redirect(home)
