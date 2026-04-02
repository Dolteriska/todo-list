from django.urls import path

from todo.views import (
    index,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView, toggle_task_status,
)


urlpatterns = [
    path("", index, name="index"),
    path("tag/list/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/toggle-status/", toggle_task_status, name="task-toggle-status"),
]

app_name = "todo"