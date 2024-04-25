from django import forms
from django.forms import DateTimeInput

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tag"]
        widgets = {
            "deadline": DateTimeInput(attrs={"type": "datetime-local"}),
        }
