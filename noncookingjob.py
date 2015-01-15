from job import *

class NoncookingJob(Job):
	def __init__(self, name, prefs, maxMatches):
		Job.__init__(self, name, prefs, maxMatches)