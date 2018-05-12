class Course():

	def __init__(self, course_name, course_acronyms, university,\
		faculty, faculty_acronyms, semester, audience):
		
		self.course_name = course_name
		self.course_acronyms = course_acronyms
		self.university = university
		self.faculty = faculty
		self.faculty_acronyms = faculty_acronyms
		self.semester = semester
		self.audience = audience
	
	def related_to_search_term(self, search_term):

		if search_term.lower() in self.course_name.lower():
			
			return True
		
		for course_acronym in self.course_acronyms:
			
			if search_term.lower() in course_acronym.lower():

				return True


		return False

	def display_in_search(self):
		pass
