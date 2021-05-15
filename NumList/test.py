from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException


class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def wait_rows_in_list_table(self,row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('listTable')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.set()-start_time >MAX_WAIT:
					raise e
					time.sleep(0.5)

	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		#self.browser.get('http://localhost:8000/')
		self.assertIn('Employees History',self.browser.title)
		header_Text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Employees Name', header_Text)
		
		inputtext = self.browser.find_element_by_id('newFirst')
		self.assertEqual(inputtext.get_attribute('placeholder'), 'First name')
		inputtext.click()
		inputtext.send_keys('Jhoanna Marie')
		time.sleep(1)

		inputlast = self.browser.find_element_by_id('newLast')
		self.assertEqual(inputlast.get_attribute('placeholder'), 'Last name')
		inputlast.click()
		inputlast.send_keys('Lopez')
		time.sleep(1)

		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(2)

		inputvalidID = self.browser.find_element_by_id('validEntry')
		self.assertEqual(inputvalidID.get_attribute('placeholder'), 'Name of ID')
		inputvalidID.click()
		inputvalidID.send_keys('TIN ID')
		time.sleep(1)

		inputvalidnum = self.browser.find_element_by_id('validNumber')
		self.assertEqual(inputvalidnum.get_attribute('placeholder'), 'ID Number')
		inputvalidnum.click()
		inputvalidnum.send_keys('123-456-000-789')
		time.sleep(1)

		inputdate = self.browser.find_element_by_id('validDate')
		self.assertEqual(inputdate.get_attribute('placeholder'), 'mm/dd/yyyy')
		inputdate.click()
		inputdate.send_keys('08/27/2020')
		time.sleep(1)
		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(2)

		#def test_browser_title(self):
		#self.browser.get('http://localhost:8000/')
		#self.assertIn('Employees Valid ID Number',self.browser.title)

		#self.wait_rows_in_list_table('1: TIN ID')
		#time.sleep(2)
		#this page should update and show two types of id on the list
		'''time.sleep(.1)
		valID = self.browser.find_element_by_id('validEntry')
		self.assertEqual(valID.get_attribute('placeholder'), 'Name of ID')
		valID.click()
		valID.send_keys('Philhealth ID')
		time.sleep(.1)
		valNum = self.browser.find_element_by_id('validNumber')
		self.assertEqual(valNum.get_attribute('placeholder'), 'ID Number')
		valNum.click()
		valNum.send_keys('12-334455007-8')
		time.sleep(.1)
		date = self.browser.find_element_by_id('validDate')
		self.assertEqual(date.get_attribute('placeholder'), 'mm/dd/yyyy')
		date.click()
		date.send_keys('09/13/2020')
		time.sleep(.1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		#self.wait_rows_in_list_table('1:TIN ID')
		#self.wait_rows_in_list_table("2:Philhealth ID")
		#time.sleep(2)
		#self.check_for_rows_in_listtable('1: TIN ID 123-456-000-789 on 08/27/2020')
		#self.check_for_rows_in_listtable("1: Philhealth ID 12-334455007-8 on 09/13/2020")
		#table = self.browser.find_element_by_id('listTable')
		#rows = table.find_element_by_tag_name('tr')
		#self.assertIn('1: TIN ID 123-456-000-789 on 08/27/2020', [row.text for row in rows])
		#self.assertIn("1: Philhealth ID 12-334455007-8 on 09/13/2020", [row.text for row in rows])'''

		'''inputbox2 = self.browser.find_element_by_id('validNumber')
		self.assertEqual(inputbox2.get_attribute('placeholder'), 'ID Number')
		inputbox2.click()
		time.sleep(1)
		inputbox2.send_keys('123-456-000-789')
		time.sleep(1)
		inputbox3 = self.browser.find_element_by_id('validDate')
		self.assertEqual(inputbox3.get_attribute('placeholder'), 'mm/dd/yyyy')
		inputbox3.click()		time.sleep(1)
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


#if __name__=='__main__':
	#unittest.main()

#browser = webdriver.Firefox ()
#browser.get('http://127.0.0.1:9900')


	'''def check_for_row_in_listtable(self,row_text):
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])'''