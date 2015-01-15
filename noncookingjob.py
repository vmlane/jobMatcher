from job import *

class NoncookingJob(Job):
	def __init__(self, name, prefs, maxMatches):
		Job.__init__(self, name, prefs, maxMatches)
		# sort all the people by number of semesters cooked, high to low
		prefs.sort(key=lambda x: x.semsCooked, reverse=True)
