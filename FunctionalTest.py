from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_browser_title(self):
		self.browser.get('http://localhost:8000/')
		self.assertIn('Employees Valid ID Number',self.browser.title)

	def check_for_rows_in_listtable(self,row_text):
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000/')
		self.assertIn('Employees Valid ID Number',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Employees Valid ID Number', headerText)
		inputbox = self.browser.find_element_by_id('validEntry')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Name of ID')
		
		employees = self.browser.find_element_by_id('newFirst')
		employees.click()
		time.sleep(1)
		employees.send_keys('Jhoanna Marie')
		time.sleep(1)
		empLast = self.browser.find_element_by_id('newLast')
		empLast.click()
		time.sleep(1)
		empLast.send_keys('Lopez')
		time.sleep(1)
		validID = self.browser.find_element_by_id('validEntry')
		validID.click()
		time.sleep(1)
		validID.send_keys('TIN ID')
		time.sleep(1)
		IDNum = self.browser.find_element_by_id('validNumber')
		IDNum.click()
		time.sleep(1)
		IDNum.send_keys('123-456-000-789')
		time.sleep(1)
		IDDate = self.browser.find_element_by_id('validDate')
		IDDate.click()
		time.sleep(1)
		IDDate.send_keys('08/27/2020')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(2)
		#this page should update and show two types of id on the list
		validID = self.browser.find_element_by_id('validEntry')
		validID.click()
		time.sleep(1)
		validID.send_keys('Philhealth ID')
		time.sleep(1)
		IDNum = self.browser.find_element_by_id('validNumber')
		IDNum.click()
		time.sleep(1)
		IDNum.send_keys('12-334455007-8')
		time.sleep(1)
		IDDate = self.browser.find_element_by_id('validDate')
		IDDate.click()
		time.sleep(1)
		IDDate.send_keys('09/13/2020')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(2)
		#self.check_for_rows_in_listtable('1: TIN ID 123-456-000-789 on 08/27/2020')
		#self.check_for_rows_in_listtable("1: Philhealth ID 12-334455007-8 on 09/13/2020")
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_element_by_tag_name('tr')
		#self.assertIn('1: TIN ID 123-456-000-789 on 08/27/2020', [row.text for row in rows])
		#self.assertIn("1: Philhealth ID 12-334455007-8 on 09/13/2020", [row.text for row in rows])






		'''inputbox2 = self.browser.find_element_by_id('validNumber')
		self.assertEqual(inputbox2.get_attribute('placeholder'), 'ID Number')
		inputbox2.click()
		time.sleep(1)
		inputbox2.send_keys('123-456-000-789')
		time.sleep(1)
		inputbox3 = self.browser.find_element_by_id('validDate')
		self.assertEqual(inputbox3.get_attribute('placeholder'), 'mm/dd/yyyy')
		inputbox3.click()
		time.sleep(1)
		inputbox3.send_keys('08/27/2020')
		time.sleep(1)'''
		
		#btnConfirm = self.browser.find_element_by_id('btnConfirm')
		#btnConfirm.click()

		#inputbox.send_keys(Keys.ENTER)
		#time.sleep(1)
		#table = self.browser.find_element_by_id('listTable')
		#rows = table.find_element_by_tag_name('tr')
		#self.assertIn('1: TIN ID 123-456-000-789', [row.text for text in rows])
		#self.assertTrue(any(row.text=='1: TIN ID'))
		#self.fail('Finish the test')


if __name__=='__main__':
	unittest.main()

#browser = webdriver.Firefox ()
#browser.get('http://127.0.0.1:9900')


	'''def check_for_row_in_listtable(self,row_text):
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])'''