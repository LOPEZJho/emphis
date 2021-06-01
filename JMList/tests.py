'''
from django.urls import resolve
from django.test import TestCase
from JMList.views import homepage
from django.template.loader import render_to_string
from django.http import HttpRequest
from JMList.models import Employee, ValidID

#item si employee
#list si validID

class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Employee.objects.count(),0)

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		validid_ = ValidID.objects.create()
		response = self.client.get(f'/JMList/{validid_.id}/')
		self.assertTemplateUsed(response, 'idlist.html')

	def test_displays_all_list_items(self):
		validid_ = ValidID.objects.create()
		Employee.objects.create(ValID='Jhoanna Marie', validid=validid_)
		Employee.objects.create(ValID='Lopez', validid=validid_)

	def test_passes_correct_list_to_template(self):
		other_validid = ValidID.objects.create()
		correct_validid = ValidID.objects.create()
		response = self.client.get(f'/JMList/{correct_validid.id}/')
		self.assertEqual(response.context['validid'], correct_validid)

class NewValidEmployeeTest(TestCase):

	def test_redirects_POST(self):
		response = self.client.post('/JMList/new', data={'newEmployee':'A new newEmployee','newAddress':'A new newAddress','newGender':'A new newGender','newPhoneNumber':'A new newPhoneNumber','newEmailAddress':'A new newEmailAddress','validEntry':'A new validEntry','validNumber':'A new validNumber','validDate':'A new validDate'})
		new_employee = Employee.objects.first()
		self.assertRedirects(response, f'/JMList/{new_employee.id}/')

class NewEmployeeTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_employee(self):
		other_employee = Employee.objects.create()
		correct_employee = Employee.objects.create()
		
		self.client.post(f'/JMList/{correct_validid.id}/AddValidID', data={'newEmployee':'A new newEmployee','newAddress':'A new newAddress','newGender':'A new newGender','newPhoneNumber':'A new newPhoneNumber','newEmailAddress':'A new newEmailAddress','validEntry':'A new validEntry','validNumber':'A new validNumber','validDate':'A new validDate'})

		self.assertEqual(Employee.objects.count(),1)
		new_employee = Employee.objects.first()
		self.assertEqual(new_employee.Name, '')
		self.assertEqual(new_employee.ValidID, correct_validid)

	def test_redirects_to_list_view(self):
		other_validid = ValidID.objects.create()
		correct_validid = ValidID.objects.create()
		response = self.client.post(f'/JMList/{correct_validid.id}/add_item', data={'newEmployee':'A new newEmployee','newAddress':'A new newAddress','newGender':'A new newGender','newPhoneNumber':'A new newPhoneNumber','newEmailAddress':'A new newEmailAddress','validEntry':'A new validEntry','validNumber':'A new validNumber','validDate':'A new validDate'})
		self.assertRedirects(response, f'/JMList/{correct_validid.id}/')



class ORMTest(TestCase):
	def test_saving_retrieving_validid(self):
		validid_ = ValidID()
		validid_.save()

		first_employee = Employee()
		first_employee.Name = 'The first (ever) list employee'
		first_employee.validid = validid_
		first_employee.save()

		second_employee = Employee()
		second_employee.Name = 'Employee the second'
		second_employee.validid = validid_
		second_employee.save()


		saved_validid = ValidID.objects.first()
		self.assertEqual(saved_validid, validid_)

		saved_employee = Employee.objects.all()
		self.assertEqual(saved_employee.count(),2)

		first_saved_employee = saved_employee[0]
		second_saved_employee = saved_employee[1]
		self.assertEqual(first_saved_employee.Name, 'The first (ever) list employee')
		self.assertEqual(first_saved_employee.validid, validid_)
		self.assertEqual(second_saved_employee.Name, 'Employee the second')
		self.assertEqual(second_saved_employee.validid, validid_)

'''

'''

		txtItem1 = Item()
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
