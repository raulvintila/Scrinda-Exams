from .course import Course

class CourseDB():

	predefined_courses = [
			{
				'course_name' : 'Grafica Inginereasca',
				'course_acronyms': ["GI"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},	
			{
				'course_name' : 'Introducere in Informatica',
				'course_acronyms': ["II"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
			{
				'course_name' : 'Matematica 2',
				'course_acronyms': ["Mate 2", "M2"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
			{
				'course_name' : 'Psihologie Educationala',
				'course_acronyms': ["Psihologie"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
			{
				'course_name' : 'Matematica 1',
				'course_acronyms': ["Mate 1", "M1"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
			{
				'course_name' : 'Utilizarea Sistemelor de Operare',
				'course_acronyms': ["USO"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
			{
				'course_name' : 'Proiectare Logica',
				'course_acronyms': ["PL"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
			{
				'course_name' : 'Programarea Calculatoarelor',
				'course_acronyms': ["PC"],
				'university': 'Politehnica Bucuresti',
				'faculty' : 'Automatica si Calculatoare',
				'faculty_acronyms': ["Automatica", "Calculatoare", "ACS"],
				'semester' : 1,
				'audience' : 'Anul 1', 
			},
		]

	def __init__(self, loaded_courses):
		
		self.courses = []

		for loaded_course in loaded_courses:
			
			course = Course(
					loaded_course['course_name'],
					loaded_course['course_acronyms'],
					loaded_course['university'],
					loaded_course['faculty'],
					loaded_course['faculty_acronyms'],
					loaded_course['semester'],
					loaded_course['audience'])

			self.courses.append(course)

	def search_courses(self, search_term):
		
		related_courses = []

		for course in self.courses:

			if course.related_to_search_term(search_term):

				related_courses.append(course)

		return related_courses
