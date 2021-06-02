from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
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
		self.assertIn('Employees History', header_Text)
		
		inputName = self.browser.find_element_by_id('newEmployee')
		self.assertEqual(inputName.get_attribute('placeholder'), 'Full name')
		inputName.click()
		inputName.send_keys('Jhoanna Marie Lopez')
		time.sleep(1)

		inputAddress = self.browser.find_element_by_id('newAddress')
		self.assertEqual(inputAddress.get_attribute('placeholder'), 'Address')
		inputAddress.click()
		inputAddress.send_keys('Windsor Homes Subd., Brgy. Burol III, Dasmarinas City, Cavite')
		time.sleep(1)

		inputGender = self.browser.find_element_by_id('newGender')
		self.assertEqual(inputGender.get_attribute('placeholder'), 'Gender')
		inputGender.click()
		inputGender.send_keys('Female')
		time.sleep(1)

		inputPhoneNumber = self.browser.find_element_by_id('newPhoneNumber')
		self.assertEqual(inputPhoneNumber.get_attribute('placeholder'), 'Phone Number')
		inputPhoneNumber.click()
		inputPhoneNumber.send_keys('09478766415')
		time.sleep(1)

		inputEmailAddress = self.browser.find_element_by_id('newEmailAddress')
		self.assertEqual(inputEmailAddress.get_attribute('placeholder'), 'Email Address')
		inputEmailAddress.click()
		inputEmailAddress.send_keys('jhoannamarie.lopez@gsfe.tupcavite.edu.ph')
		time.sleep(1)

		btnProceed = self.browser.find_element_by_id('btnProceed')
		btnProceed.click()
		time.sleep(2)

		inputValID = self.browser.find_element_by_id('validEntry')
		self.assertEqual(inputValID.get_attribute('placeholder'), 'Name of ID')
		inputValID.click()
		inputValID.send_keys('TIN ID')
		time.sleep(1)

		inputValNum = self.browser.find_element_by_id('validNumber')
		self.assertEqual(inputValNum.get_attribute('placeholder'), 'ID Number')
		inputValNum.click()
		inputValNum.send_keys('123-456-000-789')
		time.sleep(1)

		#inputdate = self.browser.find_element_by_id('validDate')
		#self.assertEqual(inputdate.get_attribute('placeholder'), 'mm/dd/yyyy')
		#inputdate.click()
		#inputdate.send_keys('08/27/2020')
		#time.sleep(1)
		
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