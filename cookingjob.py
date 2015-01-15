from job import *

class CookingJob(Job):
	def __init__(self, name, prefs, maxMatches=2):
		Job.__init__(self, name, prefs, maxMatches)