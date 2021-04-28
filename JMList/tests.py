from django.test import TestCase
from django.http import HttpResponse
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_homepage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data={'newFirst': 'A New entry'})
		self.assertIn('A New entry', response.content.decode())
		self.assertTemplateUsed(response,'homepage.html')



	'''def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_save_POST_request(self):
		reponse = self.client.post('/', data={'validEntry': 'frenzy'}) 
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'frenzy')

	def test_redirects_POST(self):
		reponse = self.client.post('/', data={'validEntry': 'frenzy'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_template_display_list(self):
		Item.objects.create(text='List item 1')
		Item.objects.create(text='List item 2')
		response = self.client.get('/')
		self.assertIn('List item 1', response.content.decode())
		self.assertIn('List item 2', response.content.decode())'''

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
