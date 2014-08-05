class Clock():
	def __init__(self, hours = 0, minutes = 0):
		self.hours = hours
		self.minutes = minutes
	
	#to use this method we need to do "classname.classmethod()"
	@classmethod	
	def at(cls, hours, minutes = 0):
# 		if hours >= 0 or hours < 24:
# 			hour = hours
# 		if minutes >= 0 or minutes < 61 :
# 			minute = minutes
		return cls(hours, minutes)	
	
	def __str__(self):
		if self.hours >= 10:
			hour = str(self.hours)
		elif self.hours < 10:
			hour = "0" + str(self.hours)
		if self.minutes >= 10:
			minute = str(self.minutes)
		elif self.minutes < 10:
			minute = "0" + str(self.minutes)
		return hour + ":" + minute
	
	def __add__(self, other):
		total_minutes = self.hours*60 + self.minutes + other
		total_hours = total_minutes/60
		if total_hours >= 24:
			#figure out how far over we are
			days_over = total_hours / 24
			final_hours = total_hours - (days_over * 24)
		else: 
			final_hours = total_hours
		final_minutes = total_minutes % 60
		return  Clock(final_hours, final_minutes)
	
	def __sub__(self, other):
		new_hours = other/60
		new_minutes = other % 60
		temp_minutes = self.minutes - new_minutes
		if temp_minutes < 0:
			final_minutes = 60 + temp_minutes
			temp_hours = self.hours - 1
		temp_hours -= new_hours
		if temp_hours < 0:
			print "Temp hours: %d" % temp_hours
			final_hours = (24 * (temp_hours / -24) ) - temp_hours
		return Clock(final_hours, final_minutes)
		
print Clock.at(00,13)-14