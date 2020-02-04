from django.shortcuts import render, redirect

# Create your views here.
from main.models import Todo


def index(request):
    todo_items = Todo.objects.all().order_by('end_date')

    context = {
        'todo_items': todo_items
    }
    return render(request, 'main/index.html', context)


def add_todo(request):
    if request.method == 'POST':
        text = request.POST['text']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        # priority = str(request.POST['priority'])

        Todo.objects.create(text=text, start_date=start_date, end_date=end_date)
        return redirect('main:index')
    else:
        return render(request, 'main/add_todo.html')


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.text = request.POST['text']
        todo.start_date = request.POST['start_date']
        todo.end_date = request.POST['end_date']
        # todo.priority = str(request.POST['priority'])
        todo.save()
        return redirect('main:index')
    else:
        context = {
            'todo': todo
        }
        return render(request, 'main/update_todo.html', context)


def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('main:index')
