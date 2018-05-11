from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# John has heard about a cool website where he can find 
		# past exams, samples and other usefull materials. He goes
		# to check out it's homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention exam resources
		self.assertIn('Resurse pentru examene', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Resurse pentru examene', header_text)

		# He is invited to enter a course name
		inputbox = self.browser.find_element_by_id('home_course_search')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Introdu un curs pentru care vrei resurse'
		)

		# He types "Proiectare Logica" into a text box
		inputbox.send_key('Proiectare logica')

		# When he hits enter, he is redirected to a new page
		# that display search results for his query
		inputbox.send_keys(Keys.Enter)
		time.sleep(1)

		self.assertIn('Cursuri gasite', self.browser.title)

		# The new page contains a search result that matches
		# the course he wanted to find
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
