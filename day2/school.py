#add a student's name to the roster for a grade
	#"add jim to grade 2"
	#Ok.

#Get a list of all students enrolled in a grade
	#Which students are in grade 2?
	#We've only got Jim just now

#Get a sorted list of all students in all grades.  Grades should sort as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name
	#Who all is enrolled in school right now?
	#grade 1: Anna, Barb, and charlie.  Grade 2: Alex, peter and Zoe.  Grade 3:..."

#Students only have one name.  

#first things first, create the school class
class School():
	def __init__(self, name):
		self.name = name
		self.db = {} #this is the data base of students.  It's a dictionary
	
	def add(self, student_name, student_grade):
		print "Add %s to grade %d at %s." % (student_name, student_grade, self.name)
		if not self.db.has_key(student_grade):
			self.db[student_grade] = {student_name}
		else:
			self.db[student_grade].add(student_name)
		print "Ok."
	
	def grade(self, grade_level):
		if grade_level in self.db:
			return self.db[grade_level]
		else: 
			return None 
	
	def sort(self):
		return self.db
			
	#The next two lines will print the school name if I just do "print school"
	def __str__(self):
		return self.name
	
	

# school = School("Haleakala Hippy School")
# school.add("Dalston", 2)
# school.add("Jay", 2)
# print school
# print school.db
