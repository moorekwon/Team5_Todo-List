from django.shortcuts import render, redirect

# Create your views here.
from main.filters import SearchFilter
from main.models import Todo, TodoStatus


def index(request):
    search_text = request.GET.get('search_text')
    query = Todo.objects.all()
    if search_text:
        todo_items = query.filter(text__contains=search_text)
    else:
        todo_items = query

    context = {
        'todo_items': todo_items,
    }
    return render(request, 'main/index.html', context)


def add_todo(request):
    if request.method == 'POST':
        author = request.user
        text = request.POST['text']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        Todo.objects.create(author=author, text=text, start_date=start_date, end_date=end_date)
        return redirect('main:index')
    else:
        return render(request, 'main/add_todo.html')


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.text = request.POST['text']
        todo.start_date = request.POST['start_date']
        todo.end_date = request.POST['end_date']
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


def check_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if todo.status:


    else:
        TodoStatus.objects.create(todo=todo, status=status)
    return redirect('main:index')
