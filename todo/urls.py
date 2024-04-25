from django.urls import path
from todo.views import (IndexView, IndexCreateView, IndexUpdateView,
                        TaskCompleteView, TaskUndoView, IndexDeleteView,
                        TagListView, TagCreateView, TagUpdateView, TagDeleteView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", IndexCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", IndexUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", IndexDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
    path("<int:pk>/undo/", TaskUndoView.as_view(), name="task-undo"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    ]

app_name = "todo"
