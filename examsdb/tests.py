from django.urls import resolve
from django.test import TestCase
from examsdb.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):

	def test_uses_home_template(self):
		
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')
		
	def test_searching_to_redirect_to_new_page(self):
		
		response = self.client.post('/',\
			data={'course_search': 'Proiectare Logica'})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/search/')
		
class SearchPageTest(TestCase):

	def test_displays_search_term(self):

		response = self.client.get('/search/?course_search=Proiectare+Logica')
		self.assertContains(response, 'S-a cautat cursul: Proiectare Logica')
