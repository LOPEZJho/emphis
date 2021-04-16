'''
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from JMList.views import home_page

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve ('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_return_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>Student List</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))'''

from django.test import TestCase
from django.http import HttpResponse
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_homepage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')