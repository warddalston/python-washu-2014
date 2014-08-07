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
		try:
			student_grade = int(student_grade)
		except:
			print "Oops! " + str(student_grade) + " isn't a valid grade at this school."
			raise Exception 
		print "Add %s to grade %d at %s. Ok" % (student_name, student_grade, self.name)
		if not self.db.has_key(student_grade):
			self.db[student_grade] = set()
		self.db[student_grade].add(student_name)
	
	def grade(self, grade_level):
		print "Which students are enrolled in grade %d?" % grade_level
		if grade_level in self.db:
			print "We've got %s right now." % ", ".join(self.db[grade_level])
			return self.db[grade_level]
		else: 
			print "No one's in this grade!"
			return None 
	
	def sort(self):
		print "Who all is enrolled at %s right now?" % self.name
		for student_grade in self.db:
			self.db[student_grade] = tuple(sorted(self.db[student_grade]))
			print "grade " + str(student_grade) + ": " + ", ".join(self.db[student_grade]) + ". "
		return self.db
			
	#The next two lines will print the school name if I just do "print school"
	def __str__(self):
		return self.name
	
	
# 
# school = School("Haleakala Hippy School")
# school.add("Dalston", 2)
# school.add("Jay", 2)
# school.add("Tommy", 3)
# school.add("Ian", 3)
# school.add("Jan", 1)
# school.add("Frank", 10)
# school.add("Frank", "pi")

# print school
# print school.db
# school.sort()
# school.grade(2)