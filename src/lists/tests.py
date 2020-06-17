from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from mysite.views import home

# Create your tests here.

class HomePage(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home(request)
		# self.assertTrue(response.content.startswith(b'<html>'))
		# self.assertIn(b'<title>To-Do lists</title>', response.content)
		# self.assertTrue(response.content.endswith(b'</html>'))
		excepted_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), excepted_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home(request)

		self.assertIn('A new list item', response.content.decode())
