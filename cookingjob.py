from job import *

class CookingJob(Job):
	def __init__(self, name, prefs, latestArrival=4.5, maxMatches=2):
		Job.__init__(self, name, prefs, maxMatches)
		self.latestArrival = latestArrival
		# remove anyone who cannot arrive before 4:30 and anyone who cannot cook that day
		self.prefs = filter(lambda x:  x.arrivalTimes[self.name] != 'minimal' and x.arrivalTimes[self.name] < latestArrival, self.prefs)
		# sort remainder based on semesters cooked (low to high) and within those groups, the tim they can arrive
		self.prefs.sort(key=lambda x: (x.semsCooked,x.arrivalTimes[self.name]))
