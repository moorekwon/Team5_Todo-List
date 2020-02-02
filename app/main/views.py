from django.shortcuts import render, redirect

# Create your views here.
from main.models import Todo


def index(request):
    todo_items = Todo.objects.all().order_by('-start_date')

    context = {
        'todo_items': todo_items
    }
    return render(request, 'main/index.html', context)


def add_todo(request):
    text = request.POST['text']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    priority = str(request.POST['priority'])
    status = str(request.POST['status'])

    Todo.objects.create(text=text, start_date=start_date, end_date=end_date, priority=priority,
                        status=status)

    print('priority >>> ', priority)
    print('status >>> ', status)
    return redirect('main:index')


def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('main:index')


