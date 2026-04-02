from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskCreationForm, TagCreationForm, TaskUpdateForm, TagUpdateForm
from todo.models import Tag, Task

def index(request):
    tasks = Task.objects.all().order_by("status", "-datetime")

    context = {
        "tasks": tasks,
    }
    return render(request, "index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task_create.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag_list.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "task_update.html"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "task_confirm_delete.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagUpdateForm
    template_name = "tag_update.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "tag_confirm_delete.html"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "tag_create.html"
    form_class = TagCreationForm
    success_url = reverse_lazy("todo:tag-list")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return redirect("todo:index")
