from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from .forms import TaskForm
from .models import Tag, Task


class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    queryset = (
        Task.objects.all().order_by("-created_at")
    )
    paginate_by = 5


class IndexCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class IndexUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class IndexDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_list_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TaskUpdateView(View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:index")
