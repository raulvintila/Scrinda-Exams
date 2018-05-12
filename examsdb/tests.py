from django.urls import resolve
from django.test import TestCase
from examsdb.views import home_page
from django.template.loader import render_to_string
from .course import Course
from .coursedb import CourseDB

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

class CourseClassTest(TestCase):

	def initialize_course1(self):

		self.course1 = Course('Proiectare Logica', ['PL'],
			'Politehnica Bucuresti', 'Automatica si Calculatoare',
			['Automatica', 'Calculatoare', 'ACS'], 1, 'Anul 1')

	def test_related_to_search_term__search_term_in_course_name(self):
		
		self.initialize_course1()
		self.assertTrue(self.course1.related_to_search_term("Proiectare Logica"))

	def test_related_to_search_term__search_term_in_course_acronyms(self):
		
		self.initialize_course1()
		self.assertTrue(self.course1.related_to_search_term("PL"))

class CourseDatabaseClassTest(TestCase):

	def load_pl_pc(self):

		self.loaded_course = [
							{
								'course_name' : 'Matematica 1',
								'course_acronyms': ['Mate 1', 'M1'],
								'university': 'Politehnica Bucuresti',
								'faculty' : 'Automatica si Calculatoare',
								'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"], 
								'semester' : 1,
								'audience' : 'Anul 1',
							},
							{
								'course_name' : 'Matematica 2',
								'course_acronyms': ['Mate 2', 'M2'],
								'university': 'Politehnica Bucuresti',
								'faculty' : 'Automatica si Calculatoare',
								'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],						
								'semester' : 1,
								'audience' : 'Anul 1',
							},
						]
				
	def test_search_courses__1_search_result(self):
		
		self.load_pl_pc()

		courseDB = CourseDB(self.loaded_course)

		search_results = courseDB.search_courses('Matematica 1')

		self.assertTrue(len(search_results) == 1)
