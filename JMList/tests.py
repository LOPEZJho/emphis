from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from JMList.views import mainpage

class HomePageTest(TestCase):
	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve ('/')
		self.assertEqual(found.func, mainpage)

	def test_mainpage_return_correct_html(self):
		request = HttpRequest()
		response = mainpage(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>Student List</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))