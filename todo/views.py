from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect,get_object_or_404
from django.views import View
from .models import TodoItem
from .forms import TodoForm


# クラスベースのビュー

class TodoListView(View):
    def get(self,request):
        todo = TodoItem.objects.all()
        return render(request, 'todo/todo_list.html', {'todos': todo})
    
class TodoCreateView(View):
    def get(self, request):
        form = TodoForm()
        return render(request, "todo/todo_create.html", {"form": form})

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
        return render(request, "todo/todo_create.html", {"form": form})

class TodoCompleteView(View):
    def get(self, request,todo_id):
        todo = get_object_or_404(TodoItem, id=todo_id)
        todo.completed = True
        todo.save()
        return redirect('todo_list')
    
class TodoUnCompleteView(View):
    def get(self, request,todo_id):
        todo = get_object_or_404(TodoItem, id=todo_id)
        todo.completed = False
        todo.save()
        return redirect('todo_list')

class TodoUpdateView(View):
    def get(self,request,todo_id):
        todo = get_object_or_404(TodoItem, id=todo_id)
        form = TodoForm(instance=todo)
        return render(request,"todo/update_todo.html",{"form": form})

    def post(self,request,todo_id):
        todo = get_object_or_404(TodoItem, id=todo_id)
        if request.method == 'POST':
            form = TodoForm(request.POST,instance=todo)
            if form.is_valid():
                form.save()
                return redirect('todo_list')
        else:
            form = TodoForm(instance=todo)
        return render(request, 'todo/update_todo.html', {'form': form, 'todo': todo})

class TodoDeleteView(View):
     def get(self,request,todo_id):
        todo = get_object_or_404(TodoItem, id=todo_id)
        return render(request, "todo/todo_delete.html", {"todo": todo})
     
     def post(self,request,todo_id):
        todo = get_object_or_404(TodoItem, id=todo_id)
        todo.delete()
        return redirect('todo_list')
            
todo_list = TodoListView.as_view()
todo_create = TodoCreateView.as_view()
complete_todo = TodoCompleteView.as_view()
uncomplete_todo = TodoUnCompleteView.as_view()
todo_update = TodoUpdateView.as_view()
todo_delete = TodoDeleteView.as_view()

