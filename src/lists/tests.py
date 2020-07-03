from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from mysite.views import home
from django.template.loader import render_to_string
import re
from .models import Item

# Create your tests here.

class HomePage(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

	#add a function to the post request test function
	def remove_csrf_tag(self, text):
		"""Remove csrf tag from TEXT"""
		return re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', text)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home(request)
		# self.assertTrue(response.content.startswith(b'<html>'))
		# self.assertIn(b'<title>To-Do lists</title>', response.content)
		# self.assertTrue(response.content.endswith(b'</html>'))
		
		# expected_html = render_to_string(
		# 	'home.html',
		# 	{'new_item_text': 'A new list item'}
		# )
		# self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home(request)

		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'}
		)
		self.assertEqual(
			self.remove_csrf_tag(response.content.decode()),
        	self.remove_csrf_tag(expected_html)
        )

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item, 'The first (ever) list item')
		self.assertEqual(second_saved_item, 'Item the second')
