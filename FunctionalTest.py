from selenium import webdriver
import unittest



class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_browser_title(self):
		self.browser.get('http://localhost:8000/')
		self.assertIn('Student List',self.browser.title)

if __name__=='__main__':
	unittest.main()

#browser = webdriver.Firefox ()
#browser.get('http://127.0.0.1:9900')
