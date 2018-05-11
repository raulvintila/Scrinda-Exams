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
		inputbox.send_keys('Proiectare logica')

		# When he hits enter, he is redirected to a search results page
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.assertIn('Cautare cursuri', self.browser.title)

		# The search page contains the searched course and a search result
		search_term = self.browser.find_element_by_id('queried_course')
		self.assertIn('Proiectare logica', search_term.text)
		
		search_results = self.browser.find_element_by_class_name('search_result')
		self.assertIn('Proiectare logica', search_results.text)
	
		# He clicks the first search result
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
