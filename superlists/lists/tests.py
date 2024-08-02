# from django.urls import resolve
from django.test import TestCase
# from django.template.response import response
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from lists.views import home_page
from lists.models import Item
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
    def test_can_save_a_Post_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    # def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        # response = self.client.get('/')
        # html = response.content.decode('utf8')
        # excepted_html  = render_to_string('home.html')
        # self.assertEqual(html,excepted_html)
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>',html)
        # self.assertTrue(html.endswith('</html>'))
        # self.assertTemplateUsed(response, 'wrong.html')

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        seconed_item = Item()
        seconed_item.text = 'Item the second'
        seconed_item.save()
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        seconed_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(seconed_saved_item.text, 'Item the second')