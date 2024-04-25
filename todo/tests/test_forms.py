from django.test import TestCase
from todo.models import Task, Tag
from todo.forms import TaskForm


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="tag1")
        self.tag2 = Tag.objects.create(name="tag2")

    def test_form(self):
        form_data = {
            "content": "Test task",
            "deadline": "2024-04-30T15:30",
            "is_done": False,
            "tag": [self.tag1.id, self.tag2.id]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            "content": "",
            "deadline": "2024-04-30T15:30",
            "is_done": False,
            "tag": [self.tag1.id, self.tag2.id]
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
