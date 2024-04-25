from django.test import TestCase

from todo.models import Task, Tag


class ModelsTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test tag")
        self.assertEqual(str(tag), "Test tag")

    def test_create_task_str(self):
        task = Task.objects.create(
            content="Read a book",
        )
        self.assertEqual(str(task), task.content)
