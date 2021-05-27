from django.urls import resolve
from django.test import TestCase
from JMList.views import homepage
from django.template.loader import render_to_string
from django.http import HttpRequest
from JMList.models import Empoyee, ValidID

class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(),0)

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		list_ = List.objects.create()
		response = self.client.get(f'/JMList/{list_.id}/')
		self.assertTemplateUsed(response, 'idlist.html')

	def test_displays_all_list_items(self):
		list_ = List.objects.create()
		Item.objects.create(valID='Jhoanna Marie', list=list_)
		Item.objects.create(valID='Lopez', list=list_)

	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get(f'/JMList/{correct_list.id}/')
		self.assertEqual(response.context['list'], correct_list)

class NewListTest(TestCase):

	def test_redirects_POST(self):
		response = self.client.post('/JMList/new', data={'newFirst':'A new newFirst','newLast':'A new newLast','validEntry':'A new validEntry','validNumber':'A new validNumber','validDate':'A new validDate'})
		new_list = List.objects.first()
		self.assertRedirects(response, f'/JMList/{new_list.id}/')

class NewItemTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		
		self.client.post(f'/JMList/{correct_list.id}/add_item', data={'newFirst': 'A new existing newFirst','newLast': 'A new newLast','validEntry': 'A new validEntry','validNumber': 'A new validNumber','validDate': 'A new validDate'})

		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, '')
		self.assertEqual(new_item.list, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.post(f'/JMList/{correct_list.id}/add_item', data={'newFirst':'A new newFirst','newLast':'A new newLast','validEntry':'A new validEntry','validNumber':'A new validNumber','validDate':'A new validDate'})
		self.assertRedirects(response, f'/JMList/{correct_list.id}/')



class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()


		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, list_)





		'''txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(),2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text,'Item one')
		self.assertEqual(savedItem2.text,'Item two')'''
	


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
