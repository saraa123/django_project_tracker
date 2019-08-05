from django.test import TestCase
from .models import Item
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
    
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_new_item.html")

    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_issue.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
    
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "create a test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_edit_an_item(self):
        item = Item(name="create a test")
        item.save()
        id = item.id 

        response = self.client.post("/edit/{0}".format(id), {"name": "a different name"})
        item = get_object_or_404(Item, pk=1)
         
        self.assertEqual("a different name", item.name)
